import sqlite3

try:
    sqlite_connection = sqlite3.connect('./world_all.db')
    cursor = sqlite_connection.cursor()
    sqlite_connection.execute('''CREATE TABLE country
               (id_country INTEGER PRIMARY KEY AUTOINCREMENT, name_country varchar(50) ,capital varchar(50), callingCodes varchar (10), 
               population int (20), area int (10), flag VARCHAR(512))''')
    sqlite_connection.execute('''CREATE TABLE language
               (id_lang INTEGER PRIMARY KEY AUTOINCREMENT, languages varchar(50), id_country int(10))''')
    sqlite_connection.execute('''CREATE TABLE location
               (id_region INTEGER PRIMARY KEY AUTOINCREMENT, region varchar(50), id_country int(10))''')
except sqlite3.Error as error:
    print("Ошибка при подключение к базе данных", error)
finally:
    if(sqlite_connection):
        sqlite_connection.close()
        print("Соединение с базой данных закрыто")
