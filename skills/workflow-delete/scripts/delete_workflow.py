import argparse
import requests
import sys
from urllib.parse import urljoin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fire_host_url", required=True)
    parser.add_argument("--access_token", required=True)
    parser.add_argument("--workflow_id", required=True, type=int)
    args = parser.parse_args()

    base = args.fire_host_url.rstrip("/") + "/"
    url = urljoin(base, f"api/v1/workflows/{args.workflow_id}")

    headers = {
        "Accept": "application/json",
        "token": args.access_token
    }

    # print(f"DELETE {url}")

    try:
        response = requests.delete(url, headers=headers, timeout=30)

        # print(f"HTTP Status: {response.status_code}")

        body = response.text.strip()

        # SUCCESS CASE (raw text or empty)
        if response.status_code in (200, 204):
            # print("\nSUCCESS RESPONSE:")
            if body:
                print(body)
            else:
                print("<empty response body>")
            return

        # FAILURE CASE (JSON error response)
        # print("\nERROR RESPONSE:")
        if body:
            try:
                print(response.json())  # failure is JSON
            except ValueError:
                print(body)
        else:
            print("<empty error response>")

        sys.exit(1)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("Error: Connection failed.")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()