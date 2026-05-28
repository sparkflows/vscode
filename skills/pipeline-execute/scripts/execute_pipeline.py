import argparse
import requests
import subprocess
import sys
import json
import os
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fire_host_url", required=True)
    parser.add_argument("--access_token", required=True)
    parser.add_argument("--pipeline_name", required=True)
    parser.add_argument("--project_id", required=True, type=int)
    parser.add_argument("--email_on_failure")
    parser.add_argument("--email_on_success")
    parser.add_argument("--lib_jars")
    parser.add_argument("--workflow_parameters")
    parser.add_argument("--spark_config")
    args = parser.parse_args()

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, "api/v1/executePipeline")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "token": args.access_token
    }

    params = {
        "pipelineName": args.pipeline_name,
        "projectId": args.project_id,
    }

    payload = {}

    if args.email_on_failure is not None:
        payload["emailOnFailure"] = args.email_on_failure
    if args.email_on_success is not None:
        payload["emailOnSuccess"] = args.email_on_success
    if args.lib_jars is not None:
        payload["libJars"] = args.lib_jars
    if args.workflow_parameters is not None:
        payload["workflowParameters"] = args.workflow_parameters
    if args.spark_config is not None:
        payload["sparkConfig"] = args.spark_config

    try:
        response = requests.post(url, headers=headers, params=params, json=payload)
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code} - {json.dumps(response.json(), indent=2)}")
            sys.exit(1)
        pipeline_execution_id = response.text.strip()
        print(f"Pipeline {pipeline_execution_id} executed")
        status_script = os.path.join(os.path.dirname(__file__), "pipeline_execution_status.py")
        subprocess.run(
            [sys.executable, status_script,
             "--fire_host_url", args.fire_host_url,
             "--access_token", args.access_token,
             "--pipeline_execution_id", pipeline_execution_id],
            check=True
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
