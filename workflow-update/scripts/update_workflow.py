#!/usr/bin/env python3
"""
Update a workflow via the API.
"""

import argparse
import json
import sys
import requests
from urllib.parse import urljoin


def parse_args():
    parser = argparse.ArgumentParser(
        description="Update a workflow via PUT /api/v1/workflows"
    )
    parser.add_argument("--workflow_json_path", required=True, metavar="PATH")
    parser.add_argument("--project_id", required=True, type=int, metavar="ID")
    parser.add_argument("--workflow_id", required=True, type=int, metavar="ID")
    parser.add_argument("--fire_host_url", required=True, metavar="URL")
    parser.add_argument("--access_token", required=True, metavar="TOKEN")
    parser.add_argument("--comment", default="", metavar="TEXT")
    return parser.parse_args()


def load_workflow(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        sys.exit(f"Error: workflow JSON file not found: {path}")
    except json.JSONDecodeError as exc:
        sys.exit(f"Error: failed to parse workflow JSON file: {exc}")


def main():
    args = parse_args()

    workflow = load_workflow(args.workflow_json_path)

    payload = {
        "analysisflowId": args.workflow_id,
        "comment": args.comment,
        "projectId": args.project_id,
        "workflow": workflow,
    }

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, "api/v1/workflows")

    headers = {
        "token": args.access_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    print(f"PUT {url}")
    print(f"  analysisflowId : {args.workflow_id}")
    print(f"  projectId      : {args.project_id}")
    print()

    try:
        response = requests.put(url, headers=headers, json=payload, timeout=60)
    except requests.exceptions.ConnectionError as exc:
        sys.exit(f"Error: could not connect to {url}\n{exc}")
    except requests.exceptions.Timeout:
        sys.exit(f"Error: request to {url} timed out")

    print(f"Status: {response.status_code}")

    try:
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print(response.text)

    if not response.ok:
        sys.exit(1)


if __name__ == "__main__":
    main()