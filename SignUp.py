# Author: Nusaiba Mahmood
# File: Screen_01a_SignUp.py

# import everything from tkinter module
from tkinter import *

import SignIn


class SignUp:
    def __init__(self,gui):
        """ User Interface in the constructor function """
        self.gui = gui
        self.frame = Frame(gui)
        self.welcomeLabel = Label(self.frame, text=" Sign Up ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.welcomeLabel.grid(row=0, column=1, padx=5, pady=5, sticky="s")

        self.usernameLabel = Label(self.frame, text="Create Username:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.usernameLabel.grid(row=2, column=0, pady=1, padx=1, sticky="e")
        self.userName = Entry(self.frame, width=30)
        self.userName.grid(row=2, column=1, pady=3)

        self.passwordLabel = Label(self.frame, text="Create Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.passwordLabel.grid(row=4, column=0, pady=1, padx=1, sticky="e")
        self.password = Entry(self.frame, width=30)
        self.password.grid(row=4, column=1, pady=3)

        self.passwordVerLabel = Label(self.frame, text="Re-enter Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.passwordVerLabel.grid(row=6, column=0, pady=1, padx=1, sticky="e")
        self.passwordVer = Entry(self.frame, width=30)
        self.passwordVer.grid(row=6, column=1, pady=3)

        # create buttons and place at a particular
        # location inside the root window
        # when user press the button, the command or
        # function affiliated to that button is executed

        self.signInButton = Button(self.frame, text=' Sign Up ', font=("Arial BOLD", 11), fg='black', bg='light goldenrod', height=1,
                              width=20,command=self.switch)
        self.signInButton.grid(row=7, column=1, pady=1)
        self.frame.configure(background="#404040", width="800", height="500")
        self.frame.columnconfigure((0, 2), weight=1, uniform="anything")
        self.frame.rowconfigure((0, 8), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

    def switch(self):

        # self.frame.forget()
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()

    def rais(self):
        self.frame.tkraise()


if __name__ == "__main__":
    gui = Tk()
    gui.geometry("800x500")

    # start the GUI
    win = SignUp(gui)
    gui.mainloop()
