import argparse
import json
import sys
import requests
from urllib.parse import urljoin


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline_json_path", required=True, metavar="PATH")
    parser.add_argument("--project_id", required=True, type=int, metavar="ID")
    parser.add_argument("--pipeline_id", required=True, type=int, metavar="ID")
    parser.add_argument("--fire_host_url", required=True, metavar="URL")
    parser.add_argument("--access_token", required=True, metavar="TOKEN")
    return parser.parse_args()


def load_pipeline(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        sys.exit(f"Error: pipeline JSON file not found: {path}")
    except json.JSONDecodeError as exc:
        sys.exit(f"Error: failed to parse pipeline JSON file: {exc}")


def main():
    args = parse_args()

    pipeline = load_pipeline(args.pipeline_json_path)

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, "createOrUpdatePipeline")

    headers = {
        "token": args.access_token,
        "projectId": str(args.project_id),
        "pipelineId": str(args.pipeline_id),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, json=pipeline, timeout=60)
    except requests.exceptions.ConnectionError as exc:
        sys.exit(f"Error: could not connect to {url}\n{exc}")
    except requests.exceptions.Timeout:
        sys.exit(f"Error: request to {url} timed out")

    if response.ok:
        print("Pipeline updated successfully.")
    else:
        try:
            print(json.dumps(response.json(), indent=2))
        except ValueError:
            print(response.text)
        sys.exit(1)


if __name__ == "__main__":
    main()
