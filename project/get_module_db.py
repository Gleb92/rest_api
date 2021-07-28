import requests
import json
from requests.api import request


class data_db_country()


class RequestBuilder:

    def init(self):
        self.response = None

    def get_request(self):
        resp = requests.get("https://restcountries.eu/rest/v2/all")
        self.response = resp.text
