"""
API client file created to assist handling
HTTP requests to Language Tool
"""

import requests
from requests.exceptions import HTTPError


class APIClient:
    """
    A client class to centralize HTTP requests
    """

    def __init__(self, base_url, username, apikey):
        self.base_url = base_url
        self.username = username
        self.apikey = apikey

        print(f"Client ready to talk to {self.base_url}")

    def get(self, endpoint):
        """
        Function dedicated to retrieve
        supported languages of LanguageTool
        """

        full_url = f"{self.base_url}{endpoint}"

        headers = {"accept": "application/json"}

        request_args = {"url": full_url, "timeout": 5, "headers": headers}

        try:
            response = requests.get(**request_args)
            response.raise_for_status()
            print("2xx Success!")
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            if http_err.response is not None:
                print(f"Status: {http_err.response.status_code}")
                print(f"Server Response: {http_err.response.text}")
            return None

    def post(self, endpoint, language, data):
        """
        Perform POST request to check the text
        """

        full_url = f"{self.base_url}{endpoint}"

        body = ""

        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        if isinstance(data, str):
            body = {
                "text": data,
                "language": language,
                "username": self.username,
                "apiKey": self.apikey,
            }
        elif isinstance(data, (dict, list)):
            body = {
                "data": data,
                "language": language,
                "username": self.username,
                "apiKey": self.apikey,
            }

        request_args = {"url": full_url, "timeout": 5, "headers": headers, "data": body}

        print(f"Attempting POST request to {self.base_url}")

        try:
            response = requests.post(**request_args)
            response.raise_for_status()
            print("2xx Success!")
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            if http_err.response is not None:
                print(f"Status: {http_err.response.status_code}")
                print(f"Server Response: {http_err.response.text}")
            return None
