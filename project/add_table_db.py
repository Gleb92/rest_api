import connecction_db
from con import connecction_db 
cur = con.cursor()
cur.execute('''CREATE TABLE country
               (id, name_country,capital, callingCodes, population, area, flag )''')
cur.execute('''CREATE TABLE language
               (id_lang, languages)''')
cur.execute('''CREATE TABLE location
               (id_region, region)''')
con.commit()
con.close()