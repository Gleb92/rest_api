import requests
import json


class contry_data():
    def __init__(self):
        pass


class Request_api:
    def __init__(self):
        self.response = None
        self.json_data = None
        self.data = None

    def get_request(self):
        resp = requests.get("https: // restcountries.eu/rest/v2/all")
        self.response = resp.text

    def parsed_json(self):
        parsed_json = json.loads(self.response)
        self.json_data = parsed_json

    def change_data(self):
        index = 0
        for values in self:
            country_name = self.json_data[index]["name"]
