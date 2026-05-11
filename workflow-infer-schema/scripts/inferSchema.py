#!/usr/bin/env python3
"""
inferSchema.py

Infers the output schema for one or more nodes in a workflow JSON and
updates the workflow via the update_workflow.py script.

Node IDs in the workflow JSON are strings (e.g. "1", "2"), so all ID
handling in this script uses strings throughout.

Usage:
    # Specific nodes
    python inferSchema.py \
        --workflow_json_path workflow.json \
        --node_ids 1 2 \
        --host_url https://example.com \
        --project_id 42 \
        --token my-access-token \
        --workflow_id 7

    # Auto-detect starting nodes (no --node_ids)
    python inferSchema.py \
        --workflow_json_path workflow.json \
        --host_url https://example.com \
        --project_id 42 \
        --token my-access-token \
        --workflow_id 7
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import requests


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Infer output schema for workflow nodes and update the workflow."
    )
    parser.add_argument(
        "--workflow_json_path",
        required=True,
        metavar="PATH",
        help="Path to the workflow JSON file.",
    )
    parser.add_argument(
        "--node_ids",
        nargs="+",
        type=str,           # IDs are strings in the workflow JSON (e.g. "1", "2")
        metavar="ID",
        default=None,
        help="Optional list of node IDs to infer schema for. "
             "If omitted, all qualifying starting nodes are used.",
    )
    parser.add_argument(
        "--host_url",
        required=True,
        metavar="URL",
        help="Base host URL for the API (e.g. https://example.com).",
    )
    parser.add_argument(
        "--project_id",
        required=True,
        type=int,
        metavar="ID",
        help="Project ID.",
    )
    parser.add_argument(
        "--token",
        required=True,
        metavar="TOKEN",
        help="Access token passed in the request header.",
    )
    parser.add_argument(
        "--workflow_id",
        required=True,
        type=int,
        metavar="ID",
        help="Workflow ID used when calling update_workflow.py.",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Workflow helpers
# ---------------------------------------------------------------------------

def load_workflow(path: str) -> dict:
    """Load and return the workflow JSON from disk."""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_workflow(path: str, workflow: dict) -> None:
    """Write the (modified) workflow JSON back to disk."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(workflow, fh, indent=2)


def build_node_map(workflow: dict) -> dict:
    """
    Return a dict of node_id (str) -> node object for every node in the workflow.

    The workflow JSON stores IDs as strings, e.g.:
        { "id": "1", "name": "Read CSV", ... }
    """
    return {str(node["id"]): node for node in workflow.get("nodes", [])}


def get_starting_node_ids(workflow: dict, node_map: dict) -> list:
    """
    Return the IDs of nodes that have no incoming edges (i.e. root / source nodes).

    Edge objects use "source" and "target" as string IDs, e.g.:
        { "source": "1", "target": "3", "id": 1, ... }
    """
    nodes_with_incoming = set()
    for edge in workflow.get("edges", []):
        # "target" is the canonical key per the workflow JSON structure
        target = edge.get("target") or edge.get("targetId") or edge.get("to")
        if target is not None:
            nodes_with_incoming.add(str(target))

    return [nid for nid in node_map if nid not in nodes_with_incoming]


# ---------------------------------------------------------------------------
# Node field helpers
# ---------------------------------------------------------------------------

def has_infer_schema_button(node: dict) -> bool:
    """
    Return True if the node has a field with name='schema' and title='InferSchema'.

    Example matching field from the workflow JSON:
        {
            "name": "schema",
            "title": "InferSchema",
            "widget": "tab",
            ...
        }
    """
    for field in node.get("fields", []):
        if field.get("name") == "schema" and field.get("title") == "InferSchema":
            return True
    return False


def inject_schema_into_node(node: dict, schema: dict) -> None:
    """
    Write the inferred column arrays into the node's outputColNames,
    outputColTypes, and outputColFormats fields.

    The workflow JSON stores these field values as JSON-encoded strings, e.g.:
        { "name": "outputColNames", "value": "[]", ... }

    After injection the value becomes a JSON-encoded string of the real array, e.g.:
        { "name": "outputColNames", "value": "[\"id\", \"price\"]", ... }
    """
    field_value_map = {
        "outputColNames":   json.dumps(schema.get("colNames", [])),
        "outputColTypes":   json.dumps(schema.get("colTypes", [])),
        "outputColFormats": json.dumps(schema.get("colFormats", [])),
    }

    for field in node.get("fields", []):
        fname = field.get("name")
        if fname in field_value_map:
            field["value"] = field_value_map[fname]


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def validate_node_ids_exist(requested_ids: list, node_map: dict) -> None:
    """Fail fast if any requested node ID does not exist in the workflow."""
    missing = [nid for nid in requested_ids if nid not in node_map]
    if missing:
        _fail(
            f"The following node IDs do not exist in the workflow: {missing}"
        )


def validate_nodes_have_infer_schema(node_ids: list, node_map: dict) -> None:
    """Fail fast if any target node is missing the InferSchema button."""
    missing_button = [
        f"{node_map[nid].get('name', 'Unknown')} (ID: {nid})"
        for nid in node_ids
        if not has_infer_schema_button(node_map[nid])
    ]
    if missing_button:
        _fail(
            "The following nodes do not have an 'Infer Schema' button: "
            + ", ".join(missing_button)
        )


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def fetch_node_schema(
    host_url: str,
    node_id: str,
    project_id: int,
    token: str,
    workflow: dict,
) -> dict:
    """
    POST to the infer-schema output API for a single node and return
    the parsed JSON response.

    Endpoint: {host_url}/api/v1/nodes/{node_id}/schema/output?projectId={project_id}
    Header:   token: <access_token>
    Body:     full workflow JSON
    """
    url = f"{host_url.rstrip('/')}/api/v1/nodes/{node_id}/schema/output"
    params = {"projectId": project_id}
    headers = {
        "token": token,
        "Content-Type": "application/json",
    }
    response = requests.post(url, params=params, headers=headers, json=workflow)
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# update_workflow.py caller
# ---------------------------------------------------------------------------

def call_update_workflow(
    workflow_json_path: str,
    project_id: int,
    workflow_id: int,
    host_url: str,
    token: str,
) -> None:
    """
    Delegate the final save to update_workflow.py, which lives in the same
    directory as this script.
    """
    script_path = (
    Path(__file__).resolve().parents[2]
    / "workflow-update"
    / "scripts"
    / "update_workflow.py"
)
    if not script_path.exists():
        _fail(f"update_workflow.py not found at expected path: {script_path}")

    cmd = [
        sys.executable,
        str(script_path),
        "--workflow_json_path", workflow_json_path,
        "--project_id",         str(project_id),
        "--workflow_id",        str(workflow_id),
        "--fire_host_url",      host_url,
        "--access_token",       token,
    ]

    _log("Calling update_workflow.py ...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout, end="")
    if result.returncode != 0:
        stderr_msg = result.stderr.strip() if result.stderr else "(no stderr)"
        _fail(f"update_workflow.py exited with code {result.returncode}:\n{stderr_msg}")


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _log(msg: str) -> None:
    print(f"[INFO] {msg}")


def _fail(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()

    # ------------------------------------------------------------------
    # Load workflow
    # ------------------------------------------------------------------
    _log(f"Loading workflow from: {args.workflow_json_path}")
    try:
        workflow = load_workflow(args.workflow_json_path)
    except FileNotFoundError:
        _fail(f"Workflow file not found: {args.workflow_json_path}")
    except json.JSONDecodeError as exc:
        _fail(f"Workflow file is not valid JSON: {exc}")

    node_map = build_node_map(workflow)

    # ------------------------------------------------------------------
    # Determine target node IDs
    # ------------------------------------------------------------------
    if args.node_ids:
        # ---- Case 1: caller specified explicit node IDs ---------------
        # Normalise to strings to match how the workflow JSON stores them
        requested_ids = [str(nid) for nid in args.node_ids]
        _log(f"Node IDs provided: {requested_ids}")

        validate_node_ids_exist(requested_ids, node_map)
        validate_nodes_have_infer_schema(requested_ids, node_map)

        target_ids = requested_ids

    else:
        # ---- Case 2: auto-detect starting nodes ----------------------
        _log("No node IDs specified — auto-detecting starting nodes ...")

        starting_ids = get_starting_node_ids(workflow, node_map)
        if not starting_ids:
            _fail("No nodes found in the workflow.")

        # Keep only those that actually have the InferSchema button
        target_ids = [
            nid for nid in starting_ids
            if has_infer_schema_button(node_map[nid])
        ]

        if not target_ids:
            _log(
                "No starting nodes with an 'Infer Schema' button were found. "
                "Nothing to do."
            )
            sys.exit(0)

        readable = [
            f"{node_map[nid].get('name', 'Unknown')} (ID: {nid})"
            for nid in target_ids
        ]
        _log(
            f"Auto-detected {len(target_ids)} qualifying starting node(s): "
            + ", ".join(readable)
        )

    # ------------------------------------------------------------------
    # Fetch schemas for ALL target nodes before modifying anything
    # ------------------------------------------------------------------
    _log("Fetching output schemas from API ...")
    schemas = {}

    for node_id in target_ids:
        node_name = node_map[node_id].get("name", "Unknown")
        _log(f"  -> {node_name} (ID: {node_id})")
        try:
            schema = fetch_node_schema(
                host_url=args.host_url,
                node_id=node_id,
                project_id=args.project_id,
                token=args.token,
                workflow=workflow,
            )
        except requests.HTTPError as exc:
            _fail(
                f"API returned an error for node '{node_name}' (ID: {node_id}): "
                f"{exc.response.status_code} {exc.response.text}"
            )
        except requests.RequestException as exc:
            _fail(
                f"Network error while fetching schema for node "
                f"'{node_name}' (ID: {node_id}): {exc}"
            )

        schemas[node_id] = schema
        _log(f"     colNames  : {schema.get('colNames')}")
        _log(f"     colTypes  : {schema.get('colTypes')}")
        _log(f"     colFormats: {schema.get('colFormats')}")

    # ------------------------------------------------------------------
    # Inject schemas into workflow JSON
    # ------------------------------------------------------------------
    _log("Injecting schemas into workflow JSON ...")
    for node in workflow.get("nodes", []):
        node_id = str(node["id"])
        if node_id in schemas:
            inject_schema_into_node(node, schemas[node_id])
            _log(f"  + {node.get('name', 'Unknown')} (ID: {node_id})")

    # ------------------------------------------------------------------
    # Persist updated workflow JSON to disk
    # ------------------------------------------------------------------
    try:
        save_workflow(args.workflow_json_path, workflow)
        _log(f"Updated workflow JSON saved to: {args.workflow_json_path}")
    except IOError as exc:
        _fail(f"Failed to save updated workflow JSON: {exc}")

    # ------------------------------------------------------------------
    # Delegate to update_workflow.py
    # ------------------------------------------------------------------
    call_update_workflow(
        workflow_json_path=args.workflow_json_path,
        project_id=args.project_id,
        workflow_id=args.workflow_id,
        host_url=args.host_url,
        token=args.token,
    )

    print("[SUCCESS] Schema inference and workflow update completed successfully.")


if __name__ == "__main__":
    main()