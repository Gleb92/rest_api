import country_data
import db_actions as actions
import db_actions_languages as actions1

db_actions = actions.DB_actions()
db_actions_lang = actions1.DB_actions()


def insert_db():
    country = country_data.Contry()
    data = country.collect_data()
    table = "country"
    db_actions.insert_data(table, data)


def get_country_by_alpha(alpha):
    table = "country"
    db_actions.select_data(table, alpha)


# insert_db()
# print(db_actions.select_all("country"))


def delete_country():
    table = "country"
    name_country = "Zimbab"
    db_actions.delete_data(table, name_country)


def update_date_table_country():
    table = "country"
    new_date_update = 2
    name_country = "Åland Islands"
    db_actions.update_data(table, new_date_update, name_country)


# update_date_table_country()
def insert_db_lang():
    language = country_data.languages()
    data = language.collect_language()
    table = "language"
    db_actions_lang.insert_data(table, data)


insert_db_lang()
