import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

from functions.databaseFunctions import closeDatabase, addItemDatabase, connectDatabase
def menuOptions():
    print("""
1. Adicione um novo contato
2. Exclua um contato
3. Atualize um contato
4. Pesquise um contato 
5. Liste todos os contatos
6. Sair""")
    while True:
        choice = input("Escolha uma opção: ")
        if choice in "123456":
            return choice
        else:
            print("Opção inválida. Tente novamente.")

def nameFix(name):
    return ' '.join(element.capitalize() for element in name.split())

def menuChoice():
    choice = menuOptions()
    match choice:
        case '1':
            connectDatabase()
            addContact()
            closeDatabase()
        case '2':
            connectDatabase()
            deleteContact()
            closeDatabase()
        case '3':
            connectDatabase()
            updateContact()
            closeDatabase()
        case '4':
            connectDatabase()
            searchContact()
            closeDatabase()
        case '5':

            listContacts()
            closeDatabase()
        case '6':
            connectDatabase()
            from time import sleep
            print('Saindo do programa...')
            sleep(1.5)
            exit()

def addContact():
    while True:
        nameInput = input('Nome do contato: ')
        if nameInput.strip() == '':
            print("Nome não pode ser vazio.")
        else:
            break
    name = nameFix(nameInput)
    while True:
        ddd = input('Insira o DDD: ')
        if ddd == '':
            print("DDD não pode ser vazio.")
        elif ddd.isdigit() == False:
            print("DDD deve ser numérico.")
        elif len(ddd) != 2:
            print("DDD deve ter 2 dígitos.")
        elif ddd == '00':
            print("DDD não pode ser 00.")
        else:
            break
    while True:
        phone = input('Insira o número de telefone: ')
        if phone == '':
            print("Por favor, digite um número válido.")
        elif phone.isdigit() == False:
            print("Por favor, digite um número válido.")
        elif len(phone) != 8 and len(phone) != 9:
            print("Número deve ter pelo menos 8 ou 9 dígitos.")
        else:
            break
    addItemDatabase(name, ddd, phone)
    while True:
        option = input('Deseja adicionar outro contato? (S/N) ').upper().strip()
        if option not in 'SN':
            print("Opção inválida. Tente novamente.")
        if option == 'S':
            addContact()
        else:
            break 
    
def deleteContact():
    print()

def updateContact():
    print()

def searchContact():
    print()

def listContacts():
    print()
