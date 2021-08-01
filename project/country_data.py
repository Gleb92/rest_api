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
        self.country_languages = []
        self.region = str()

    def parse(self, data):
        self.country_name = str(data["name"]).replace("'", "''")
        self.country_capital = str(
            data["capital"]).replace("'", "''")
        self.country_calling_codes = data["callingCodes"][0]
        self.country_population = data["population"]
        self.country_languages = self.parse_lang(data)
        self.country_area = data["area"]
        self.country_flag = data["flag"]
        self.region = data["region"]

    def parse_lang(self, data):
        index_name = 0
        self.country_languages = []
        count_languages = data["languages"]
        for values in count_languages:
            values = data["languages"][index_name]["name"]
            index_name += 1
            self.country_languages += [values]
        return self.country_languages

    def create_query_to_db(self, table):
        if table == "country":
            query = f"""INSERT INTO country (name_country, capital, callingCodes, population, area, flag) \
                        VALUES ('{self.country_name}', '{self.country_capital}', \
                        '{self.country_calling_codes}', '{self.country_population}', \
                        '{self.country_area}','{self.country_flag}');"""
        if table == "language":
            query_mas = []
            for values in self.country_languages:
                query_mas += [
                    f"INSERT INTO language (languages) VALUES ('{values}');"]
            query = ' '.join(query_mas)
        if table == "location":
            query = f"""INSERT INTO location (region)  VALUES ('{self.region}');"""
        return query
