import country_data
import db_actions as actions
import request_json

db_actions = actions.DB_actions()
parser = request_json.request_api()


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
    db_actions.select_data(table, "Moscow")


def get_country_by_alpha():
    table = "country"
    table2 = "language"
    db_actions.select_all(table, table2)


# print(get_country_by_alpha())
# print(get_country_by_alpha1())
# insert_db()
print(db_actions.select_all("country", "language", "location"))


def delete_country():
    table = "country"
    name_country = "Zimbab"
    db_actions.delete_data(table, name_country)


def update_date_table_country():
    table = "country"
    new_date_update = 2
    name_country = "Åland Islands"
    db_actions.update_data(table, new_date_update, name_country)
