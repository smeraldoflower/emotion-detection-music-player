# Author: Nusaiba Mahmood
# File: SignUp.py

# import everything from tkinter module
from tkinter import *

import SignIn
import db
import re
from werkzeug.security import generate_password_hash,check_password_hash


class SignUp:
    def __init__(self, gui):
        """ User Interface in the constructor function """
        self.gui = gui
        self.frame = Frame(gui)
        # self.gui.attributes('-fullscreen', True)
        width = self.gui.winfo_screenwidth()

        height = self.gui.winfo_screenheight()
        # setting tkinter window size

        self.gui.geometry("%dx%d" % (width, height))
        self.welcomeLabel = Label(self.frame, text=" Sign Up ", fg="white",
                                  bg="#404040", font=("Consolas BOLD", 30))
        self.welcomeLabel.grid(row=0, column=1, padx=5, pady=5, sticky="s")

        self.usernameLabel = Label(self.frame, text="Create Username:", fg="white",
                                   bg="#404040", font=("Arial BOLD", 12))
        self.usernameLabel.grid(row=2, column=0, pady=1, padx=1, sticky="e")
        self.userName = Entry(self.frame, width=30)
        self.userName.grid(row=2, column=1, pady=3)

        self.passwordLabel = Label(self.frame, text="Create Password:", fg="white",
                                   bg="#404040", font=("Arial BOLD", 12))
        self.passwordLabel.grid(row=4, column=0, pady=1, padx=1, sticky="e")
        self.password = Entry(self.frame,show="*", width=30)
        self.password.grid(row=4, column=1, pady=3)

        self.passwordVerLabel = Label(self.frame, text="Re-enter Password:", fg="white",
                                      bg="#404040", font=("Arial BOLD", 12))
        self.passwordVerLabel.grid(row=6, column=0, pady=1, padx=1, sticky="e")
        self.passwordVer = Entry(self.frame,show="*", width=30)
        self.passwordVer.grid(row=6, column=1, pady=3)
        self.label_auth = Label(self.frame, text="", fg="white",
                                      bg="#404040", font=("Arial BOLD", 12))

        # create buttons and place at a particular
        # location inside the root window
        # when user press the button, the command or
        # function affiliated to that button is executed

        self.signUpButton = Button(self.frame, text=' Sign Up ', font=("Arial BOLD", 11), fg='black',
                                   bg='light goldenrod', height=1, width=20, command=self.sign_up)
        self.signUpButton.grid(row=7, column=1, pady=1)
        self.label_auth.grid(row=8,column=1,sticky="n")
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

    def sign_up(self):
        username_check = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", self.userName.get())
        password_check = re.search("[^\\s]{8,}", self.password.get())
        password_ver = re.search("[^\\s]{8,}", self.passwordVer.get())
        if not username_check or not password_check:
            self.label_auth.config(text="Invalid username or password")
            print("Invalid username or password")
            return False
        if self.passwordVer.get() != self.password.get():
            self.label_auth.config(text="Password mismatch")
            print("Password mismatch")
            return False
        hashpass = self.hash_password(
            self.password.get())
        if db.signup(self.userName.get(), hashpass):
            self.switch()

    def hash_password(self,password):
        hashed_password = generate_password_hash(password)
        return hashed_password



# if __name__ == "__main__":
#     guii = Tk()
#     guii.geometry("800x500")
#
#     # start the GUI
#     win = SignUp(guii)
#     guii.mainloop()
