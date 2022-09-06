
from tkinter import *

import login


class Login_screen:

    def __init__(self):

        # Starup and defining window
        self.__login_window = Tk()
        
        # Setting up login details and buttons for login
        username_header = Label(self.__login_window, text="Username/path: ")
        password_header = Label(self.__login_window, text="Password: ")

        self.__username = Entry(self.__login_window, borderwidth=2, width=20)
        self.__password = Entry(self.__login_window, borderwidth=2, width=20, show="*")

        log_button = Button(self.__login_window, text="Log in", font=8, background="Green", foreground="White", command=self.login)
        cancel_button = Button(self.__login_window, text="Cancel", font=8, background="Red", foreground="White" ,command=self.cancel)

        # Setting up location of the buttons, entries and labels. For details see grid model in GITHUB
        username_header.grid(row=0, column=0, sticky=W+N)
        password_header.grid(row=1, column=0, sticky=E+N)

        self.__username.grid(row=0, column=1, sticky=W+N)
        self.__password.grid(row=1, column=1, sticky=E+N)

        cancel_button.grid(row=2, column=0, sticky=E+W)
        log_button.grid(row=2, column=1, sticky=E+W)


        self.__login_window.mainloop()

    def login(self):

        username = self.__username.get()
        password = self.__password.get()

        logHandler = login.Logg(username, password)

        logInfo = logHandler.login()

        access = logInfo[0]

        if access:
            print("DOES LOGINSTUFF")

        if not access:
            print("DOES NOT LOGINSTUFF")


    def cancel(self):
        self.__login_window.destroy()


p = Login_screen()

