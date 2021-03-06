import os

from login import Logg
from getpass import getpass


def check_passwords(password, password_repeated):
    while(password != password_repeated):
        # Loops untill password is same

        print('Incorrect passwords. Please retry')
        password = getpass('Password: ')
        password_repeated = getpass('Repeat password: ')

    return password



def create_user ():
    # Calls encrypter that handles the key and loads information
  
    user_name = input('Username: ')
    password = getpass('Password: ')
    password_repeated = getpass('Repeat password: ')

    password = check_passwords(password, password_repeated)

    f = open(user_name + ".txt", "x")

    firstRow = {'service': ['username', 'password']}

    logHandler = Logg(user_name, password)
    logHandler.save_into_file(firstRow)
    
    print('User', user_name, 'created succesfully.')
    login(user_name, password)

    return
    

def login (user_name='', password=''):
    # Gets logins and calls login manager

    if (user_name=='' and password==''):
        # If user is new are paswords and usernames already given

        user_name = input('Username: ')
        password = getpass('Password: ')

    logHandler = Logg(user_name, password)

    logInfo = logHandler.login()

    access = logInfo[0]
    serviceList = logInfo[1]

    if access == True: # == Users file has found...
         while after_login_menu(user_name, serviceList, logHandler):
            pass

    return

def help(loginstatus):

    if loginstatus:
        print(
        '''
        q - Log Out
        s - save
        a - Add new password
        l - list all servises available
        f - Make a search based on database
        d - Delete info
        h - Ask for help
        ''')
    
    else:
        print(
        '''
        q - Close program
        a - Register new user
        l - Login
        h - Ask for help
        ''')


def pre_login_menu():
    # Menu for a user that has not logged in

    has_login = False
    cmd = input('Cmd: ')
    cmd = cmd.lower()
    

    if(cmd == 'q'):
        # Closes program and encrypts

        print('Goodbye!')
        return False

    elif(cmd == 'a'):
        # adds new user

        create_user()

    elif(cmd == 'l'):
        # Login

        login()

    elif(cmd == 'h'):
        # Help
        help(has_login)
    
    else:
        print('Erroneus command. Try again')
       
    return True


def add_new_password(services):
    # Adds new password

    service_name = input('Url/Service: ')
    user_name = input('Username: ')
    password = getpass('Password: ')
    password_repeated = getpass('Repeat password: ')

    # Check passwords
    password = check_passwords(password, password_repeated)

    # Add created password to list
    services[service_name] = user_name, password

    print('Password added succesfully.')

def list_of_services(services):
    # Prints list of services required

    print('Following services have been registered: ')
    print("")

    for key, value in services.items():
        # Go through dictionary and print out every password

        print(key, ' : ', value)

    print()

def make_search(services):
    # Get password from chosen service

    service_name = input('Search for password by typing service name: ')

    i = 0

    for key, value in services.items():
        # Go through dictionary, try to find right key and print it

        if key.find(service_name) != -1:
            # Check if dictionary key has typed string in it

            if i == 0:
                # First time print

                print("service  :  [username  :  password]")
                print()

            print(key, ' : ', value)

            i = i + 1

    if i == 0:
        # If cannot find any service, then print

        print("cannot find service called: " + service_name)

    else:
        print()
        return


def delete(services):
    # Deletes chosen password
    
    service_name = input('Delete by typing service name: ')
    for key, value in services.items():
        # Go trough dictionary, try to find right key and delete it

        if key == service_name:
            services.pop(key)
            return

    print("cannot find service called: " + service_name)


def after_login_menu(user_name, serviceList, logHandler):

    has_login = True
    cmd_txt = 'Logged as "' + user_name + '"  Cmd: '
    cmd = input(cmd_txt)
    cmd = cmd.lower()
    

    if(cmd == 'q'):
        # Closes program and encrypts
        status = logHandler.save_into_file(serviceList)

        if status:
            print('Saved and login out...')
        
        else:
            print('An error occurred while saving. Login out...')

        return False

    elif(cmd == 'a'):
        # adds new password

        add_new_password(serviceList)

    elif(cmd == 'l'):
        # Lists of services

        list_of_services(serviceList)

    elif(cmd == 'f'):
        # Make a search by service

        make_search(serviceList)

    elif(cmd == 'd'):
        # Delete service from the database:

        delete(serviceList)

    elif(cmd == 's'):
        # Save current state:
        status = logHandler.save_into_file(serviceList)
        os.system("attrib -h " + user_name + ".txt")

        if status:
            print('Saved!')
        
        else:
            print('An error occurred while saving.')

    elif(cmd == 'h'):
        # Help
        help(has_login)
    
    else:
        print('Erroneus command. Try again')
       

    return True    


def ui():
    
    print('Welcome to p4ssw0rd manager 0.01')

    while pre_login_menu():
        pass
    
    return

ui()