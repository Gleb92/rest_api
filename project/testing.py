import country_data
import db_actions as actions

db_actions = actions.DB_actions()


def insert_db():
    country = country_data.Contry()
    data = country.collect_data()

    table = "country"
    db_actions.insert_data(table, data)


def get_country_by_alpha(alpha):
    table = "country"
    db_actions.select_data(table, alpha)


insert_db()
# print(db_actions.select_all("country"))


def delete_country():
    table = "country"
    name_country = "Zimbab"
    db_actions.delete_data(table, name_country)
