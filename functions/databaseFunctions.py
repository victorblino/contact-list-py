import sqlite3

def connectDatabase():
    try:
        sqlite3.connect('database.db')
    except sqlite3.Error as error:
        return print(f'Ocorreu um erro. Erro: {error}')

def closeDatabase():
    sqlite3.connect('database.db').close()

def commitDatabase():
    sqlite3.connect('database.db').commit()
    
def checkDatabase():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    try:
        cursor.execute("""CREATE TABLE contacts (name text, ddd integer, number integer, id integer)""")
        database.commit()
        database.close()
    except sqlite3.OperationalError:
        print("[DATABASE] ☑️ ")
    except:
        print('Ocorreu algum erro na Database.')

def countItensDatabase():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    try:
        cursor.execute("""SELECT COUNT(*) FROM contacts""")
        return cursor.fetchone()[0]
    except sqlite3.Error as error:
        print(f'Ocorreu algum erro ao contar os contatos. Erro: {error}')
    except:
        print('Ocorreu algum erro ao ver contatos cadastrados.')
    
def lastID():
    if countItensDatabase() == None:
        return 0
    else:
        return countItensDatabase()

def listContactsDatabase():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM contacts""")
    for row in sorted(cursor.fetchall()):
        print(f'Nome: {row[0]} | DDD: {row[1]} | Número: {row[2]} | ID: {row[3]}')

def addItemDatabase(name, ddd, number):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    try:
        cursor.execute("""INSERT INTO contacts (name, ddd, number, id) VALUES (?, ?, ?, ?)""", (name, ddd, number, lastID() + 1))
        database.commit()
    except sqlite3.Error as error:
        print(f'Ocorreu algum erro ao adicionar contato. Erro: {error}')

