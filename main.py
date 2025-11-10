"""
Main execution file for the Language Tool checker
"""

import os
import argparse
import sys
from api_client import APIClient


def _parse_args() -> argparse.Namespace:
    """
    Build and parse the command-line arguments
    """
    parser = argparse.ArgumentParser(description="Check a text on Language tool")
    parser.add_argument(
        "--function", required=True, help="Inform which function should be used"
    )
    parser.add_argument(
        "--language", help="Inform the language to be verified. I.E: en-US"
    )
    parser.add_argument("--text", help="Inform the text to be verified or a JSON")
    return parser.parse_args()


base_url = os.getenv("LANGUAGETOOL_BASEURL")
username = os.getenv("LANGUAGETOOL_USERNAME")
apikey = os.getenv("LANGUAGETOOL_APIKEY")

if not base_url or not apikey:
    print("APIKey or base url not set in environment variables")
    print("Please set them and try again")
    sys.exit(1)

if __name__ == "__main__":

    args = _parse_args()

    client = APIClient(base_url=base_url, username=username, apikey=apikey)
    match args.function:
        case "check":
            print(f"Getting the environemnt from {base_url}")
            result = client.post("/check", args.language, args.text)
            print(result)
        case "languages":
            print("Getting the languages supported")
            result = client.get("/languages")
            print(result)
