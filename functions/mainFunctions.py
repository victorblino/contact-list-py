def menuOptions():
    print("""
1. Adicione um novo contato
2. Exclua um contato
3. Atualize um contato
4. Pesquise um contato 
5. Liste todos os contatos
6. Sair""")
    while True:
        choice = int(input("Escolha uma opção: "))
        if choice in range(1,7):
            return choice
        else:
            print("Opção inválida!")

def menuChoice():
    choice = menuOptions()
    match choice:
        case 1:
            addContact()
        case 2:
            deleteContact()
        case 3:
            updateContact()
        case 4:
            searchContact()
        case 5:
            listContacts()
        case 6:
            exit()

def addContact():
    print()
def deleteContact():
    print()
def updateContact():
    print()
def searchContact():
    print()
def listContacts():
    print()
