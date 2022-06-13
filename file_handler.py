from encrypter import Encrypter

class FileHandler:
        # Handles file writing and reading

    def __init__(self, filename, key='samppa'):
        # Initializes file writing

        self.__filename = filename
        self.__encrypter = Encrypter(key)
        self.__filedata = {}

    def open_file(self):
        # Tries to open a file. if file not found gives an error

        try:
            # Opens a file in to read mode...
            file = open(self.__filename, mode="r")

            for encrypted_row in file:
                # Gets encrypted datarow from the file and decrypts it

                current_row = self.__encrypter.decrypt(encrypted_row) 
                current_row = current_row.strip()
                current_row_in_a_list = current_row.split(";")

                # Saves data into dict as {service: [username, password]}
                self.__filedata[current_row_in_a_list[0]] = current_row_in_a_list[1:]
                
        except OSError:
            # If opening the file fails return false/failed

            print('Fail')

        file.close()
        
  
    def write_file(self, database):
        # Tries to write in a file the current avialable database

        try:
            # Opens a file in to write mode...

            file_to_saved = open(self.__filename, mode="w")

            for current_key in database:
                # Loops thorugh known databse

                line = current_key # First to be added is servicename/key

                for current in database[current_key]:
                    # Adds login details into sentence

                    line += ';' + current 

                # Encrypts data and writes it into the file
                encrypted_line = self.__encrypter.encrypt(line) 
                print(encrypted_line, file=file_to_saved)
            
            file_to_saved.close()
                
        except OSError:
             # If writing in the file fails return false/failed

            print('Fail')

        
    def get_data(self):
        # Returns the data that was retrieved from the file after decryption
        return self.__filedata

fileobj = FileHandler('testUser.txt')

fileobj.open_file()

print(fileobj.get_data())

fileobj.write_file(fileobj.get_data())