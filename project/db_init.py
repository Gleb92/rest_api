import sqlite3

try:
    sqlite_connection = sqlite3.connect('./world_all.db')
    cursor = sqlite_connection.cursor()
    sqlite_connection.execute('''CREATE TABLE country
               (id_country int(10), name_country varchar(50) ,capital varchar(50), callingCodes int (10), 
               population int (20), area int (10), flag VARCHAR(512), PRIMARY KEY(id_country))''')
    sqlite_connection.execute('''CREATE TABLE language
               (id_lang int (10), languages varchar(50), PRIMARY KEY(id_lang))''')
    sqlite_connection.execute('''CREATE TABLE location
               (id_region int (10), region varchar(50), PRIMARY KEY(id_region))''')
except sqlite3.Error as error:
    print("Ошибка при подключение к базе данных", error)
finally:
    if(sqlite_connection):
        sqlite_connection.close()
        print("Соединение с базой данных закрыто")
