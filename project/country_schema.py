from marshmallow import Schema, fields


class CountrySchema (Schema):
    country_name = fields.Str()
    country_capital = fields.Str()
    country_calling_codes = fields.Str()
    country_area = fields.Str()
    country_population = fields.Int()
    country_flag = fields.Str()
    country_languages = fields.Str()
    region = fields.Str()
