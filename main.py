from functions.databaseFunctions import checkDatabase, closeDatabase
from functions.mainFunctions import menuChoice

checkDatabase()
try:
    menuChoice()
    closeDatabase()
except KeyboardInterrupt:
    print('\nO usuário encerrou o programa.')
finally:
    print('\nObrigado por usar o programa!')