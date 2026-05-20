import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--fire_host_url", required=True)
parser.add_argument("--access_token", required=True)
args = parser.parse_args()

response = requests.get(
    f"{args.fire_host_url.rstrip('/')}/api/v1/configurations",
    headers={"token": args.access_token}
)

data = response.json()

if not response.ok:
    print(f"An error occurred, here are the details: {data}")
else:
    for item in data:
        if item.get("confProperty", {}).get("name") == "airflow.enabled":
            value = item["confProperty"]["value1"]
            print("Airflow Enabled" if value == "true" else "Airflow Disabled")
            break
