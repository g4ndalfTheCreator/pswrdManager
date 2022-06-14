from pathlib import Path
from file_handler import FileHandler

class Logg:

    def __init__(self, user_name, password):
        # Setting up file handler and filepath    

        self.__filepath = user_name + ".txt"
        self.__filehandler = FileHandler(self.__filepath, password)

    def login(self):
        # Finding the right file and try to open it

        path = Path(self.__filepath)

        if path.is_file():
            # Check if the file exists

            # rightAccess decrypt(filepath, password)
            rightAccess = self.__filehandler.open_file()

            services = self.__filehandler.get_data()

            if rightAccess == False:

                self.wrongUserorPass()

            else:

                return True, services

        else:

            self.wrongUserorPass()

        return False, ""

    def save_into_file(self , services):
        # Saves data into file and returns if it was succesfull

        return self.__filehandler.write_file(services)


    def wrongUserorPass(self):
        # In case of wrong username or password

        print("Username or password wrong")