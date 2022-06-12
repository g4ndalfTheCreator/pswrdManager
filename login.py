import pathlib
from os import path

def logg(user_name, password):

    nyky = pathlib.Path(__file__).parent.resolve()
    nyky = str(nyky)

    filepath = nyky + "//" + user_name

    return

def main():

    logg("testUser", "testPass")

    return

if __name__ == "__main__":
    main()