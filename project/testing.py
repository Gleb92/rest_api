import seraliz
import db_actions as actions

db_actions = actions.DB_actions()


def insert_db():
    country = seraliz.contry_data()
    country.change_data()
    table = "country"
    db_actions.insert_data(table, country)


insert_db()


def get_country_by_alpha(alpha):
    table = "country"
    db_actions.select_data(table, alpha)


print(get_country_by_alpha('Mariehamn'))
