import requests
from requests.api import request

class RequestBuilder:

    def init(self):
        self.response = None

    def get_request(self):
        resp = requests.get("https://restcountries.eu/rest/v2/all")
        self.response = resp.text


request_inst = RequestBuilder()
request_inst.get_request()
print(request_inst.response)
