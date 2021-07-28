import db_actions

db_actions_select = db_actions.DB_actions()


def get_country_by_alpha(alpha):
    table = "country"
    db_actions_select.select_data(table, alpha)


print(get_country_by_alpha('Kabul'))
