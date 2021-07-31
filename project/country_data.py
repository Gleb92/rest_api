import requests
import request_json


class CountryData:
    def __init__(self):
        self.country_name = str()
        self.country_capital = str()
        self.country_calling_codes = int()
        self.country_population = int()
        self.country_area = int()
        self.country_flag = str()
        self.country_languages = str()
        self.values = int()

    def parse(self, data):
        self.country_name = str(data["name"]).replace("'", "''")
        self.country_capital = str(
            data["capital"]).replace("'", "''")
        self.country_calling_codes = data["callingCodes"][0]
        self.country_population = data["population"]
        self.country_languages = data["languages"][self.values]["name"]
        self.country_area = data["area"]
        self.country_flag = data["flag"]

    def parse_lang(self):
        index_name = 0
        count_languages = self.country_languages["languages"]
        for values in count_languages:
            index_name += 1
        return values

    def create_query_to_db(self, table):
        if table == "country":
            query = f"INSERT INTO country (name_country, capital, callingCodes, population, area, flag) \
                        VALUES ('{self.country_name}', '{self.country_capital}', \
                        '{self.country_calling_codes}', '{self.country_population}', \
                        '{self.country_area}','{self.country_flag}');"
        if table == "language":
            query = f"INSERT INTO language (languages)  VALUES ('{self.country_languages}');"
        return query
