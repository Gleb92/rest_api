import requests
import request_json

parser = request_json.request_api()


class Contry():
    def __init__(self):
        self.country_name = str()
        self.country_capital = str()
        self.country_calling_codes = int()
        self.country_population = int()
        self.country_area = int()
        self.country_flag = str()

    def collect_data(self):
        parser.get_request()
        parser.parsed_json()
        data = parser.json_data
        return data
