from os import path
import sys
sys.path.append('../project')
from flask import Flask, Request
from country_schema import CountrySchema
import request_json
import db_actions as actions
import country_data
import json


app = Flask(__name__)
db_actions = actions.DB_actions()
parser = request_json.request_api()
country = country_data.CountryData()
country_schema = CountrySchema()


def collect_data():
    parser.get_request()
    parser.parsed_json()
    data = parser.json_data
    return data


def insert_db():
    data = collect_data()
    table = "location"
    db_actions.insert_data(table, data)


def get_country_by_alpha1():
    table = "country"
    return db_actions.select_data(table, "Kabul")


def get_country_by_alpha():
    table = "country"
    table2 = "language"
    db_actions.select_all(table, table2)


# print(get_country_by_alpha())
# print(get_country_by_alpha1())
# insert_db()
#print(db_actions.select_all("country", "language", "location"))


def delete_country():
    table = "country"
    name_country = "Zimbab"
    db_actions.delete_data(table, name_country)


def update_date_table_country():
    table = "country"
    new_date_update = 2
    name_country = "Åland Islands"
    db_actions.update_data(table, new_date_update, name_country)


# def select_all_info_country():
#    return db_actions.select_all_country("Botswana")


def parse_db_response(db_response):
    country.serialize_db_response_single_object(db_response)
    db_response_dict = country_schema.dump(country)
    return db_response_dict


@app.route('/countries/')
def select_all_info():
    all_info_countries = db_actions.select_all_country_info()
    all_countries = []
    response = None
    for values in all_info_countries:
        values_country = values[0].replace("'", "''")
        countries = db_actions.select_all_country(values_country)
        info_all = parse_db_response(countries)
        all_countries.append(info_all)
    response = json.dumps(all_countries)
    return response



@app.route('/countries/<string:name>')
def select_all_info_country(name):
    db_data = db_actions.select_all_country(name)
    info = parse_db_response(db_data)
    return info

@app.route('/countries/<string:language>')
def select_all_country_by_languuage(language):
    all_info_countries = db_actions.select_all_country_language(language)
    all_countries = []
    response = None
    for values in all_info_countries:
        values_country = values[0].replace("'", "''")
        countries = db_actions.select_all_country(values_country)
        info_all = parse_db_response(countries)
        all_countries.append(info_all)
    response = json.dumps(all_countries)
    return response

@app.route('/countries/<string:population>')
def select_all_country_by_population(population):
    all_info_countries = db_actions.select_all_country_population(population)
    all_countries = []
    response = None
    for values in all_info_countries:
        values_country = values[0].replace("'", "''")
        countries = db_actions.select_all_country(values_country)
        info_all = parse_db_response(countries)
        all_countries.append(info_all)
    response = json.dumps(all_countries)
    return response


@app.route('/countries/<string:symbol>')
def select_all_country_with_starts(symbol):
    all_info_countries = db_actions.select_all_country_which_starts()
    all_countries = []
    response = None
    for values in all_info_countries:
        values_country = values[0].replace("'", "''")
        if values_country[0] == symbol:
            countries = db_actions.select_all_country(values_country)
            info_all = parse_db_response(countries)
            all_countries.append(info_all)
    response = json.dumps(all_countries)
    return response

print(select_all_country_by_population(10000000))