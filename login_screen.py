from cgitb import text
from distutils.cmd import Command
import tkinter as tk
from tkinter import *
from tkinter.ttk import Treeview

import login


class Login_screen(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
    #Switching frames

        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()
    


#Login page frame
class LoginPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        username_header = Label(self, text="Username/path: ")
        password_header = Label(self, text="Password: ")

        self.__username = tk.Entry(self, borderwidth=2, width=20)
        self.__password = tk.Entry(self, borderwidth=2, width=20, show="*")

        log_button = Button(self, text="Log in", bg='green', command=lambda: self.Login())
        cancel_button = Button(self, text="Cancel", bg='red', command=lambda: self.Cancel())
        register_new = Button(self, text="Register", bg='SteelBlue1', command=lambda: self.Register())

        username_header.grid(row=0, column=0, sticky=W + N)
        password_header.grid(row=1, column=0, sticky=E + N)

        self.__username.grid(row=0, column=1, sticky=W + N)
        self.__password.grid(row=1, column=1, sticky=E + N)

        cancel_button.grid(row=2, column=0, sticky=E + W)
        log_button.grid(row=2, column=1, sticky=E + W)
        register_new.grid(row=3, column=0, columnspan=2, sticky=E + W)

    def Login(self):
    #When login pressed

        username = self.__username.get()
        password = self.__password.get()

        logHandler = login.Logg(username, password)

        logInfo = logHandler.login()

        access = logInfo[0]
        serviceList = logInfo[1]

        if access:
        #If username and password right

            AfterLoginPage.services = serviceList
            self.master.switch_frame(AfterLoginPage)

            print("DOES LOGINSTUFF", serviceList)

        if not access:
            print("DOES NOT LOGINSTUFF")

    def Register(self):
        # Opens register window

        self.master.switch_frame(RegisterFrame)


    def Cancel(self):
        # Closes window
        self.destroy()


class RegisterFrame(tk.Frame):
    # opens new registering page
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        username_header = Label(self, text="New username/path: ")
        password_header = Label(self, text="Password: ")
        password_rp_header = Label(self, text="Repeat Password: ")

        self.__username = tk.Entry(self, borderwidth=2, width=20)
        self.__password = tk.Entry(self, borderwidth=2, width=20, show="*")
        self.__password_rp = tk.Entry(self, borderwidth=2, width=20, show="*")

        register_new = Button(self, text="Register user", bg='SteelBlue1', command=lambda: self.Register())

        username_header.grid(row=0, column=0, sticky=W + N + E)
        password_header.grid(row=1, column=0, sticky=E + N + W)
        password_rp_header.grid(row=2, column=0, sticky= E + W)

        self.__username.grid(row=0, column=1, sticky=W + N + E)
        self.__password.grid(row=1, column=1, sticky=E + N + W)
        self.__password_rp.grid(row=2, column=1, sticky = E + W)
       
        register_new.grid(row=3, column=0, columnspan=2, sticky=E + W)

    def Register(self):
        # Does actual registering
        
        username = self.__username.get()
        password = self.__password.get()
        password_rp = self.__password_rp.get()

        if password == password_rp:
            # Logins and creates new user

            f = open(username + ".txt", "x")

            firstRow = {'service': ['username', 'password']}

            logHandler = login.Logg(username, password)
            logHandler.save_into_file(firstRow)
            
            self.master.switch_frame(AfterLoginPage)

        else:
            # Show errormessages
            pass
        


class AfterLoginPage(tk.Frame):

    #Servicelist of signed in user
    services = dict

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        addNew_button   = Button(self, text="Add new",  bg='red',   command=lambda: self.AddNew())
        delete_button   = Button(self, text="Delete",   bg='red',   command=lambda: self.Delete())
        search_button   = Button(self, text="Search",   bg='red',   command=lambda: self.Search())
        listAll_button  = Button(self, text="List all", bg='red',   command=lambda: self.ListAll())
        settings_button = Button(self, text="Settings", bg='red',   command=lambda: self.Settings())
        save_button     = Button(self, text="Save",     bg='red',   command=lambda: self.Save())
        logout_button   = Button(self, text="Logout",   bg='red',   command=lambda: self.Logout())

        addNew_button.grid(row=0, column=0, sticky=E + W)
        delete_button.grid(row=0, column=1, sticky=E + W)
        search_button.grid(row=0, column=2, sticky=E + W)
        listAll_button.grid(row=0, column=3, sticky=E + W)
        settings_button.grid(row=0, column=4, sticky=E + W)
        save_button.grid(row=0, column=5, sticky=E + W)
        logout_button.grid(row=0, column=6, sticky=E + W)

    def AddNew(self):
    #Adding new user to database

        serviceName_header = Label(self, text="Url/Service: ")
        username_header = Label(self, text="Username: ")
        password_header = Label(self, text="Password: ")
        passwordRepeated_header = Label(self, text="Repeat password: ")

        self.__serviceName = tk.Entry(self, borderwidth=2, width=20)
        self.__username = tk.Entry(self, borderwidth=2, width=20)
        self.__password = tk.Entry(self, borderwidth=2, width=20)
        self.__passwordRepeated = tk.Entry(self, borderwidth=2, width=20)

        ok_button = Button(self, text="Log in", bg='green', command=lambda: self.Ok())
        cancel_button = Button(self, text="Cancel", bg='red', command=lambda: self.Cancel())

        serviceName_header.grid     (row=1, column=0, sticky=E + W)
        username_header.grid        (row=2, column=0, sticky=E + W)
        password_header.grid        (row=3, column=0, sticky=E + W)
        passwordRepeated_header.grid(row=4, column=0, sticky=E + W)
        self.__serviceName.grid     (row=1, column=1, sticky=E + W)
        self.__username.grid        (row=2, column=1, sticky=E + W)
        self.__password.grid        (row=3, column=1, sticky=E + W)
        self.__passwordRepeated.grid(row=4, column=1, sticky=E + W)
        ok_button.grid              (row=5, column=0, sticky=E + W)
        cancel_button.grid          (row=5, column=1, sticky=E + W)


        print("Adding new")

    def Delete(self):
        print("Deleting")

    def Search(self):
        print("Searching")

    def ListAll(self):
    #List of every saved password

        columns = ('Service', 'Username', 'Password')

        services_treeview = Treeview(self, columns=columns, show='headings')

        services_treeview.heading('Service', text='Services')
        services_treeview.heading('Username', text='Username')
        services_treeview.heading('Password', text='Password')

        services_treeview.grid(row=1, columnspan=7)

        for key, value in list(self.services.items())[1:]:
            services_treeview.insert('', END, values=(key, value[0], value[1]))
            print(key, ' : ', value)

    def Settings(self):

        print("Setting")

    def Save(self):

        print("Saving")

    def Logout(self):

        print("Logging out")



if __name__ == "__main__":
    app = Login_screen()
    app.mainloop()
