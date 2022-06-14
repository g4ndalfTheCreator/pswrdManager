import pathlib
from pathlib import Path
from file_handler import FileHandler


def logg(user_name, password):
    # Finding the right file and try to open it

    filepath = user_name + ".txt"

    path = Path(filepath)

    if path.is_file():
        # Check if the file exists

        # Setting up file handler
        filehandler = FileHandler(filepath, password)

        # rightAccess decrypt(filepath, password)
        rightAccess = filehandler.open_file()

        services = filehandler.get_data()

        if rightAccess == False:

             wrongUserorPass()

        else:

            return True, services

    else:

        wrongUserorPass()

    return False, ""


def wrongUserorPass():
    # In case of wrong username or password

    print("Username or password wrong")


    def main():

        logg("testUser", "samppa")

        return

    if __name__ == "__main__":
        main()