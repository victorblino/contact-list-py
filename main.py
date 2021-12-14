from functions.databaseFunctions import checkDatabase, closeDatabase
from functions.mainFunctions import menuChoice

checkDatabase()
try:
    menuChoice()
except KeyboardInterrupt:
    print('\nO usuário encerrou o programa.')
finally:
    closeDatabase()
    print('\nObrigado por usar o programa!')
