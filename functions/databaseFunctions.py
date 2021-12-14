import sqlite3

def connectDatabase():
    try:
        database = sqlite3.connect('database.db')
        database.close()
        return True
    except sqlite3.Error as error:
        return print(f'Ocorreu um erro. Erro: {error}')

def closeDatabase():
    database = sqlite3.connect('database.db')
    database.close()

def checkDatabase():
    try:
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        cursor.execute("""CREATE TABLE contacts (name text, ddd integer, number integer, id integer)""")
        database.commit()
        database.close()
    except sqlite3.OperationalError:
        print("[DATABASE] ☑️ ")
    except:
        print('Ocorreu algum erro na Database.')

def countDatabase():
    try:
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        cursor.execute("""SELECT COUNT(*) FROM contacts""")
        count = cursor.fetchone()
        database.close()
        return count[0]
    except:
        print('Ocorreu algum erro ao ver contatos cadastrados.')

def addItemDatabase(name, ddd, number):
    try:
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        cursor.execute("""INSERT INTO contacts VALUES (?, ?, ?, ?)""", (name, ddd, number, countDatabase() + 1))
        database.commit()
        database.close()
    except sqlite3.Error as error:
        print(f'Ocorreu algum erro ao adicionar contato. Erro: {error}')

