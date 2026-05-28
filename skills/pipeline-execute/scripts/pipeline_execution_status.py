import argparse
import requests
import sys
import json
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fire_host_url", required=True)
    parser.add_argument("--access_token", required=True)
    parser.add_argument("--pipeline_execution_id", required=True, type=int)
    args = parser.parse_args()

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, f"api/v1/pipelines/execution/{args.pipeline_execution_id}")

    headers = {
        "Accept": "application/json",
        "token": args.access_token
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code} - {json.dumps(data, indent=2)}")
            sys.exit(1)
        description = data['description'] or "success"
        print(f"Execution Result: {description}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
