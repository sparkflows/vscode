import os
import argparse
import requests
import sys
import json
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fire_host_url", required=True)
    parser.add_argument("--access_token", required=True)
    parser.add_argument("--workflow_id", required=True)
    args = parser.parse_args()

    base = args.fire_host_url.rstrip("/") + "/"
    workflow_id = args.workflow_id

    url = urljoin(base, f"api/v1/workflows/{workflow_id}")

    headers = {
        "Accept": "application/json",
        "token": args.access_token
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code} - {response.text}")
            sys.exit(1)

        output_dir = os.path.join(os.path.dirname(__file__), "..", "fetched-workflows")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{workflow_id}.json")

        with open(output_path, "w") as f:
            f.write(json.dumps(response.json()["workflow"], indent=2))

        print("success")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()