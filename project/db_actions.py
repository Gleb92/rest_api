import sqlite3
import db_conection


class DB_actions():

    def __init__(self):
        self.connection = db_conection.DB_Conector()

    def select_data(self, table, query_params):
        self.connection.connect_db()
        connection = self.connection.cursor
        result = connection.execute(
            f"SELECT * FROM {table} where capital = '{query_params}';").fetchall()
        return result

    def insert_data(self, table, country):
        self.connection.connect_db()
        connection = self.connection.cursor
        result = connection.execute(f"INSERT INTO {table} (name_country, capital, callingCodes, population, area, flag) \
                    VALUES ('{country.country_name}', '{country.country_capital}', \
                     '{country.country_calling_codes}', '{country.country_population}', \
                     '{country.country_area}','{country.country_flag}');")
        self.connection.connection.commit()
        return result
        # return connection.execute(f"INSERT INTO {table} (id_country, name_country, capital, callingCodes, population, area, flag) VALUES {data_to_insert};")
