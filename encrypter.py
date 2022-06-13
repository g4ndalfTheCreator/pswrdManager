import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class Encrypter(object):
    # Encrypts strings with 256 bit AES encryption. 

    def __init__(self, key):
        # Setting up block size and password

        self.__block_size = AES.block_size
        self.__key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, text):
        # Makes encryption

        text = self.pad(text)
        iv = Random.new().read(self.__block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        # Decrypts encrypted txt 

        try:
            # Tries to encode 

            encrypted_text = b64decode(encrypted_text)
            iv = encrypted_text[:self.__block_size]
            cipher = AES.new(self.__key, AES.MODE_CBC, iv)
            text = cipher.decrypt(encrypted_text[self.__block_size:]).decode("utf-8")
            return self.unpad(text)
        
        except UnicodeDecodeError:
            # If user has given wrong password 

            return 'Wrong password'


    def pad(self, text):
        # Padds text to pieces for encrypter to encrypt. Makes sure that strings are long enough

        number_of_bytes_to_pad = self.__block_size - len(text) % self.__block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = text + padding_str
        return padded_plain_text

    @staticmethod
    def unpad(text):
        # Unpads text: Makes it readable for humans

        last_character = text[len(text) - 1:]
        return text[:-ord(last_character)]

'''
encrypter = Encrypter('AadssssssssssssaDFaaaaaaaaaaaaaaaaaaaaaaaaaa')

txt = 'Nacciveneet on kivojaaAAAAAAAAAAAAAAAAAAAAAASAFAFAFFAFaafFA'

encrypted = encrypter.encrypt(txt)

print(encrypted)

# Case encrypted txt
uncrypted = encrypter.decrypt(encrypted)
print(uncrypted)

# Case wrong password
falsepss =  Encrypter('Q')
print(falsepss.decrypt(encrypted))
'''