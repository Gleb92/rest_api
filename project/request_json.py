import requests
import json


class request_api:

    def __init__(self):
        self.response = None
        self.json_data = None

    def get_request(self):
        resp = requests.get("https://restcountries.eu/rest/v2/all")
        self.response = resp.text

    def parsed_json(self):
        parsed_json = json.loads(self.response)
        self.json_data = parsed_json
