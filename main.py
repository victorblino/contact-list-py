from functions.databaseFunctions import checkDatabase
from functions.mainFunctions import menuChoice


checkDatabase()
try:
    menuChoice()
except KeyboardInterrupt:
    print('\nO usuário encerrou o programa.')