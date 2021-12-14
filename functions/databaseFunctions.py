import sqlite3

def checkDatabase():
    try:
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        cursor.execute("""CREATE TABLE contacts (name text, ddd integer, number integer)""")
        database.commit()
        database.close()
    except sqlite3.OperationalError:
        print("[DATABASE] ☑️ ")
    except:
        print('Ocorreu algum erro na Database.')