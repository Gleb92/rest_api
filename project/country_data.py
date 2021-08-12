import requests
import request_json


class CountryData:
    def __init__(self):
        self.id_country = 0
        self.country_name = str()
        self.country_capital = str()
        self.country_calling_codes = str()
        self.country_population = int()
        self.country_area = int()
        self.country_flag = str()
        self.country_languages = []
        self.region = str()

    def serialize_db_response(self, db_response):
        self.id_country = db_response[0][0]
        self.country_name = db_response[0][1]
        self.country_capital = db_response[0][2]
        self.country_calling_codes = db_response[0][3]
        self.country_population = db_response[0][4]
        self.country_area = db_response[0][5]
        self.country_flag = db_response[0][6]
        self.country_languages = self.parse_num_lang(db_response)
        print(type(self.country_languages))
        print(type(self.country_flag))
        self.region = db_response[0][8]

    def parse(self, data):
        self.id_country += 1
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

    def parse_num_lang(self, db_response):
        index_name = 0
        self.country_languages = []
        count_languages = db_response
        for values in count_languages:
            values = db_response[index_name][7]
            index_name += 1
            self.country_languages += [values]
        return self.country_languages

    def create_query_to_db(self, table):
        if table == "country":
            query = f"""INSERT INTO country (id_country, name_country, capital, callingCodes, population, area, flag) \
                        VALUES ('{self.id_country}', '{self.country_name}', '{self.country_capital}', \
                        '{self.country_calling_codes}', '{self.country_population}', \
                        '{self.country_area}','{self.country_flag}');"""
        if table == "language":
            query_mas = []
            for values in self.country_languages:
                query_mas += [
                    f"INSERT INTO language (languages, id_country) VALUES ('{values}', '{self.id_country}');"]
            query = ' '.join(query_mas)
        if table == "location":
            query = f"""INSERT INTO location (region, id_country)  VALUES ('{self.region}', '{self.id_country}');"""
        return query
