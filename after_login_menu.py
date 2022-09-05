from tkinter import *

class After_login_screen:

    def __init__(self):

        # Starup and defining window
        self.__after_login_window = Tk()

        # Setting up login details and buttons for login

        addNew_button = Button(self.__after_login_window, text="Add new", font=8, background="Green", foreground="White",
                            command=self.addNew)
        delete_button = Button(self.__after_login_window, text="Delete", font=8, background="Green", foreground="White",
                               command=self.delete)
        search_button = Button(self.__after_login_window, text="Search", font=8, background="Green", foreground="White",
                            command=self.search)
        listAll_button = Button(self.__after_login_window, text="List all", font=8, background="Green", foreground="White",
                               command=self.listAll)
        settings_button = Button(self.__after_login_window, text="Settings", font=8, background="Green", foreground="White",
                            command=self.settings)
        save_button = Button(self.__after_login_window, text="Save", font=8, background="Green", foreground="White",
                               command=self.save)
        logout_button = Button(self.__after_login_window, text="Logout in", font=8, background="Green", foreground="White",
                            command=self.logout)

        # Setting up location of the buttons, entries and labels. For details see grid model in GITHUB
        addNew_button.grid(row=0, column=0, sticky=E + W)
        delete_button.grid(row=0, column=1, sticky=E + W)
        search_button.grid(row=0, column=2, sticky=E + W)
        listAll_button.grid(row=0, column=3, sticky=E + W)
        settings_button.grid(row=0, column=4, sticky=E + W)
        save_button.grid(row=0, column=5, sticky=E + W)
        logout_button.grid(row=0, column=6, sticky=E + W)

        self.__after_login_window.mainloop()

    def addNew(self):
        print("Adding new")

    def delete(self):
        print("Deleting")

    def search(self):
        print("Searching")

    def listAll(self):
        print("Listing all")

    def settings(self):
        print("Setting things")

    def save(self):
        print("Saveing")

    def logout(self):
        print("Logging out")

p = After_login_screen()