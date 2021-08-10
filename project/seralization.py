from marshmallow import Schema, fields


class CountrySchema (Schema):
    name = fields.Str()
    capital = fields.Str()
    language = fields.Str()
    calling_codes = fields.Str()
    country_area = fields.Str()
    country_calling_codes = fields.Int()
    country_flag = fields.Str()
    language = fields.Str()
    region = fields.Str()


class CountrySerai():
    def __init__(self, country_name, country_capital, country_language, country_area, country_calling_codes, country_flag, region):
        self.id_country = 0
        self.country_name = country_name
        self.country_capital = country_capital
        self.country_language = country_language
        self.country_area = country_area
        self.country_calling_codes = country_calling_codes
        self.country_flag = country_flag
        self.country_language = country_language
        self.region = region
