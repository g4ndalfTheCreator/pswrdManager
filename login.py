import pathlib
from pathlib import Path

def logg(user_name, password):
    # Finding the right file and try to open it

    nyky = pathlib.Path(__file__).parent.resolve()
    nyky = str(nyky)

    filepath = nyky + "//" + user_name + ".txt"

    path = Path(filepath)

    if path.is_file():
        # Check if the file exists

        # rightAccess decrypt(filepath, password)

        rightAccess = True

        if rightAccess == False:

            wrongUserorPass()        

        else:

            return True

    else:

        wrongUserorPass()

    return False


def wrongUserorPass():
    # In case of wrong username or password

    print("Username or password wrong") 


def main():

    logg("testUser", "testPass")

    return

if __name__ == "__main__":
    main()