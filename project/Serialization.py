import requests
import json


class contry_data():
    def __init__(self):
        self.data = None
        self.country_name = str()
        self.country_capital = str()
        self.country_calling_codes = int()
        self.country_population = int()
        self.country_area = int()
        self.country_flag = str()

    def change_data(self):
        index = 0
        for values in self.data:
            self.country_name = self.data[index]["name"]
            self.country_capital = self.data[index]["capital"]
            print(self.country_capital)
            self.country_calling_codes = self.data[index]["callingCodes"]
            self.country_population = self.data[index]["population"]
            self.country_area = self.data[index]["area"]
            self.country_flag = self.data[index]["flag"]
            index += 1


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


parser = request_api()
parser.get_request()
parser.parsed_json()


x = contry_data()
x.data = parser.json_data


print(x.change_data())
