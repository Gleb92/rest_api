from os import path
import sys
sys.path.append('../project')
from marshmallow import Schema, fields


class CountrySchema (Schema):
    country_name = fields.Str()
    country_capital = fields.Str()
    country_calling_codes = fields.Int()
    country_area = fields.Str()
    country_population = fields.Int()
    country_flag = fields.Str()
    country_language = fields.Str
    region = fields.Str()


class CountrySerai():
    def __init__(self, id_country, country_name, country_capital, country_calling_codes, country_area, country_population, country_flag, country_language, region):
        self.id_country = id_country
        self.country_name = country_name
        self.country_capital = country_capital
        self.country_calling_codes = country_calling_codes
        self.country_area = country_area
        self.country_population = country_population
        self.country_flag = country_flag
        self.country_language = country_language
        self.region = region
