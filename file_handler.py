from encrypter import Encrypter

class FileHandler:
        # Handles file writing and reading

    def __init__(self, filename, key='samppa'):
        # Initializes file writing

        self.__filename = filename
        self.__encrypter = Encrypter(key)
        self.__filedata = {}

    def open_file(self):
        try:
            file = open(self.__filename, mode="r")

            for encrypted_row in file:

                current_row = self.__encrypter.decrypt(encrypted_row)
                current_row = current_row.strip()
                current_row_in_a_list = current_row.split(";") # Decrypter here
                self.__filedata[current_row_in_a_list[0]] = current_row_in_a_list[1:]
                
        except OSError:
            print('Fail')

        file.close()
        print(self.__filedata)
  
    def write_file(self, database):
        try:
            file_to_saved = open(self.__filename, mode="w")

            for current_key in self.__filedata:
                line = current_key
                for current in self.__filedata[current_key]:
                    line += ';' + current
                print(line)
                encrypted_line = self.__encrypter.encrypt(line) 
                print(encrypted_line, file=file_to_saved)
            
            file_to_saved.close()
                
        except OSError:
            print('Fail')

        


fileobj = FileHandler('testUser.txt')

fileobj.open_file()

fileobj.write_file(1)