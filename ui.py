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
    password = getpass.getpass('Password: ')
    password_repeated = getpass('Repeat password: ')

    password = check_passwords(password, password_repeated)
    
    print('User', user_name, 'created succesfully.')
    login(user_name, password)

    return
    

def login (user_name='', password=''):
    # Gets logins and calls login manager

    if (user_name=='' and password==''):
        # If user is new are paswords and usernames already given

        user_name = input('Username: ')
        password = getpass('Password: ')

        logInfo = Logg(user_name, password)

        access = logInfo.login()[0]
        serviceList = logInfo.login()[1]

    if access == True: # == Users file has found...
         while after_login_menu(user_name, serviceList):
            pass

    return

def help(loginstatus):

    if loginstatus:
        print(
        '''
        q - Log Out
        a - Add new password
        l - list all servises available
        s - Make a search based on database
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
    print("service  :  [username  :  password]")
    print()

    for key, value in services.items():
        #G o trough dictionary and print out everyone

        print(key, ' : ', value)

    print()

def make_search(services):
    # Get password from chosen service

    service_name = input('Search for password by typing service name: ')

    for key, value in services.items():
        # Go trough dictionary, try to find right key and print it

        if key == service_name:
            print("service  :  [username  :  password]")
            print(key, ' : ', value)

            return


    print("cannot find service called: " + service_name)


def delete(services):
    # Deletes chosen password
    
    service_name = input('Delete by typing service name: ')
    for key, value in services.items():
        # Go trough dictionary, try to find right key and delete it

        if key == service_name:
            services.pop(key)
            return

    print("cannot find service called: " + service_name)


def after_login_menu(user_name, serviceList):

    has_login = True
    cmd_txt = 'Logged as "' + user_name + '"  Cmd: '
    cmd = input(cmd_txt)
    cmd = cmd.lower()
    

    if(cmd == 'q'):
        # Closes program and encrypts

        print('Login out...')
        return False

    elif(cmd == 'a'):
        # adds new password

        add_new_password(serviceList)

    elif(cmd == 'l'):
        # Lists of services

        list_of_services(serviceList)

    elif(cmd == 's'):
        # Make a search by service

        make_search(serviceList)

    elif(cmd == 'd'):
        # Delete service from the database:

        delete(serviceList)


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