import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

from functions.databaseFunctions import closeDatabase, addItemDatabase, connectDatabase, countItensDatabase, listContactsDatabase, commitDatabase
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

def questionMenu():
    while True:
        option = input('Deseja voltar ao menu? (S/N) ').upper().strip()
        if option not in 'SN':
            print("Opção inválida. Tente novamente.")
        if option == 'S':
            menuChoice()
        else:
            break

def goMenu():
    while True:
        option = input('Deseja voltar ao menu? (S/N) ').upper().strip()
        if option not in 'SN':
            print("Opção inválida. Tente novamente.")
        if option == 'S':
            menuChoice()
        else:
            break

def nameFix(name):
    return ' '.join(element.capitalize() for element in name.split())

def menuChoice():
    choice = menuOptions()
    connectDatabase()
    match choice:
        case '1':
            addContact()
        case '2':
            deleteContact()
        case '3':
            updateContact()
        case '4':
            searchContact()
        case '5':
            listContacts()
        case '6':
            from time import sleep
            print('Saindo do programa...')
            sleep(1.5)
    closeDatabase()

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
    questionMenu()
    
def deleteContact():
    if countItensDatabase() == 0:
        print('Não há contatos para excluir.')
        goMenu()
    else: 
        listContactsDatabase()
    while True:
        IDcontact = input('Insira o ID do contato que deseja excluir: ')
        if IDcontact == '':
            print("Por favor, digite um ID válido.")
        elif IDcontact.isdigit() == False:
            print("Por favor, digite um ID válido.")
        elif countItensDatabase() < int(IDcontact):
            print("ID não existe.")
        elif int(IDcontact) == 0:
            print("Não existe nenhum contato com esse ID.")
        else:
            break
    try:
        cursor.execute(f"""DELETE from contacts WHERE id = {IDcontact}""")
        database.commit()
    except sqlite3.Error as error:
        print(f'Erro ao excluir o contato: {error}')
    while True:
        option = input('Deseja excluir outro contato? (S/N) ').upper().strip()
        if option not in 'SN':
            print("Opção inválida. Tente novamente.")
        if option == 'S':
            deleteContact()
        else:
            break
    goMenu()

def updateContact():
    if len(cursor.fetchall()) == 0:
        print('Não há contatos para atualizar.')
        goMenu()
    else:
        listContactsDatabase()
        while True:
            IDcontact = input('Insira o ID do contato que deseja atualizar:')
            if IDcontact == '':
                print("Por favor, digite um ID válido.")
            elif IDcontact.isdigit() == False:
                print("Por favor, digite um ID válido.")
            elif countItensDatabase() < int(IDcontact):
                print("ID não existe.")
            elif int(IDcontact) == 0:
                print("Não existe nenhum contato com esse ID.")
            else:
                break
        option = input("""Oque deseja atualizar?
1. Nome
2. DDD
3. Número""")
        while True:
            if option.strip() not in '123':
                print("Opção inválida. Tente novamente.")
            else:
                break
            
        match option:
            case '1':
                listContactsDatabase()
                while True:
                    IDcontact = input('Insira o ID do contato que deseja atualizar:')
                    if IDcontact == '':
                        print("Por favor, digite um ID válido.")
                    elif IDcontact.isdigit() == False:
                        print("Por favor, digite um ID válido.")
                    elif countItensDatabase() < int(IDcontact):
                        print("ID não existe.")
                    elif int(IDcontact) == 0:
                        print("Não existe nenhum contato com esse ID.")
                    else:
                        break
                while True:
                    nameInput = input('Novo nome: ')
                    if nameInput.strip() == '':
                        print("Nome não pode ser vazio.")
                    else:
                        break
                name = nameFix(nameInput)
                try:
                    cursor.execute(f"""UPDATE contacts SET name = '{name}' WHERE id = {IDcontact}""")
                    database.commit()
                except sqlite3.Error as error:
                    print(f'Erro ao atualizar o contato: {error}')
                while True:
                    option = input('Deseja atualizar outro contato? (S/N) ').upper().strip()
                    if option not in 'SN':
                        print("Opção inválida. Tente novamente.")
                    if option == 'S':
                        updateContact()
                    else:
                        break
            case '2':
                listContactsDatabase()
                while True:
                    IDcontact = input('Insira o ID do contato que deseja atualizar: ')
                    if IDcontact == '':
                        print("Por favor, digite um ID válido.")
                    elif IDcontact.isdigit() == False:
                        print("Por favor, digite um ID válido.")
                    elif countItensDatabase() < int(IDcontact):
                        print("ID não existe.")
                    elif int(IDcontact) == 0:
                        print("Não existe nenhum contato com esse ID.")
                    else:
                        break
                while True:
                    ddd = input('Novo DDD: ')
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
                try:
                    cursor.execute(f"""UPDATE contacts SET ddd = '{ddd}' WHERE id = {IDcontact}""")
                    database.commit()
                except sqlite3.Error as error:
                    print(f'Erro ao atualizar o contato: {error}')
                while True:
                    option = input('Deseja atualizar outro contato? (S/N) ').upper().strip()
                    if option not in 'SN':
                        print("Opção inválida. Tente novamente.")
                    if option == 'S':
                        updateContact()
                    else:
                        break
            case '3':
                listContactsDatabase()
                while True:
                    IDcontact = input('Insira o ID do contato que deseja atualizar: ')
                    if IDcontact == '':
                        print("Por favor, digite um ID válido.")
                    elif IDcontact.isdigit() == False:
                        print("Por favor, digite um ID válido.")
                    elif countItensDatabase() < int(IDcontact):
                        print("ID não existe.")
                    elif int(IDcontact) == 0:
                        print("Não existe nenhum contato com esse ID.")
                    else:
                        break
                while True:
                    number = input('Novo número: ')
                    if number == '':
                        print("Número não pode ser vazio.")
                    elif number.isdigit() == False:
                        print("Número deve ser numérico.")
                    elif len(number) != 8 and len(number) != 9:
                        print("Número deve ter 8 ou 9 dígitos.")
                    else:
                        break
                try:
                    cursor.execute(f"""UPDATE contacts SET number = '{number}' WHERE id = {IDcontact}""")
                except sqlite3.Error as error:
                    print(f'Erro ao atualizar o contato: {error}')
                while True:
                    option = input('Deseja atualizar outro contato? (S/N) ').upper().strip()
                    if option not in 'SN':
                        print("Opção inválida. Tente novamente.")
                    if option == 'S':
                        updateContact()
                    else:
                        break
                    
def searchContact():
    print('Sendo feito!')
    goMenu()

def listContacts():
    if countItensDatabase() == 0:
        print('Não há contatos para listar.')
        goMenu()
    else:
        listContactsDatabase()
        goMenu()