import requests
import request_josn

parser = request_josn.request_api()


class contry_data():
    def __init__(self):
        self.country_name = str()
        self.country_capital = str()
        self.country_calling_codes = int()
        self.country_population = int()
        self.country_area = int()
        self.country_flag = str()

    def change_data(self):
        parser.get_request()
        parser.parsed_json()
        data = parser.json_data
        index = 0
        for values in data:
            self.country_name = data[index]["name"]
            self.country_capital = data[index]["capital"]
            self.country_calling_codes = data[index]["callingCodes"][0]
            self.country_population = data[index]["population"]
            self.country_area = data[index]["area"]
            self.country_flag = data[index]["flag"]
            index += 1
