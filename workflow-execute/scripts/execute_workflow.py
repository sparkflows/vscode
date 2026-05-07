import argparse
import requests
import sys
import json
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fire_host_url", required=True)
    parser.add_argument("--access_token", required=True)
    parser.add_argument("--workflow_id", required=True, type=int)
    parser.add_argument("--email_on_failure")
    parser.add_argument("--email_on_success")
    parser.add_argument("--lib_jars")
    parser.add_argument("--program_parameters")
    parser.add_argument("--spark_config")
    args = parser.parse_args()

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, "api/v1/workflow/execute")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "token": args.access_token
    }

    payload = {"workflowId": args.workflow_id}

    if args.email_on_failure is not None:
        payload["emailOnFailure"] = args.email_on_failure
    if args.email_on_success is not None:
        payload["emailOnSuccess"] = args.email_on_success
    if args.lib_jars is not None:
        payload["libJars"] = args.lib_jars
    if args.program_parameters is not None:
        payload["programParameters"] = args.program_parameters
    if args.spark_config is not None:
        payload["sparkConfig"] = args.spark_config

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code} - {response.text}")
            sys.exit(1)
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()