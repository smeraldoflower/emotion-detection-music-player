# Authors: Nusaiba Mahmood, Kwame Addo, Yewande Hassan
# File: SignIn.py

import SignUp
import Welcome
import db

import re
from tkinter import *
from werkzeug.security import generate_password_hash, check_password_hash


class SignIn:
    # ---------- GUI Init Function --------- #
    def __init__(self, gui):
        self.gui = gui
        self.frame = Frame(gui)
        self.gui.attributes('-fullscreen', True)
        
        self.gui.grid_rowconfigure(0, weight=1)
        self.gui.grid_columnconfigure(0, weight=1)

        # Set the background colour of application's GUI window
        self.frame.configure(background="#404040", width=800, height=500)

        # GUI Grid configurations
        self.frame.columnconfigure((0, 2), weight=1, uniform="anything")
        self.frame.rowconfigure((0, 10), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)
        
        # Sign In Page Title
        self.signInTitleLabel = Label(self.frame, text=" Sign In ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.signInTitleLabel.grid(row=0, column=1, padx=5, pady=5, sticky="s")

        # Invalid Username or Password text
        self.label_auth = Label(self.frame, text="", fg="VioletRed1", bg="#404040", font=("Arial BOLD ITALIC", 12))
        self.label_auth.grid(row=1, column=1, sticky="n")

        # Username: Entry field
        self.usernameLabel = Label(self.frame, text="Username:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.usernameLabel.grid(row=2, column=0, pady=1, padx=1, sticky="e")
        self.userName = Entry(self.frame, width=30, font=("Arial BOLD", 11))
        self.userName.grid(row=2, column=1, pady=3)

        # Password: Entry field
        self.passwordLabel = Label(self.frame, text="Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.passwordLabel.grid(row=4, column=0, pady=1, padx=1, sticky="e")
        self.password = Entry(self.frame,show="*", width=30, font=("Arial BOLD", 11))
        self.password.grid(row=4, column=1, pady=3)

        # Blank Divider Label for ui spacing
        self.dividerLabel =Label(self.frame, text="", fg="white", bg="#404040", font=("Consolas BOLD", 11))
        self.dividerLabel.grid(row=5,column=1, pady=3)

        # Create and place buttons in the root window.
        # The function in the command attribute is executed when the button is clicked.

        # Sign In Button - Switch to Welcome Page in Welcome.py file
        self.signInButton = Button(self.frame, text=' Sign In ', font=("Arial BOLD", 11), fg='black', bg='light blue', 
                                   height=1, width=25,command=self.sign_in)
        self.signInButton.grid(row=6, column=1, pady=1)

        # Sign Up Button - Switch to Sign Up Page in SignUp.py file
        self.signUpButton = Button(self.frame, text=' Sign Up ', font=("Arial BOLD", 11), fg='black', bg='light goldenrod', 
                                   height=1, width=25,command=self.switch)
        self.signUpButton.grid(row=7, column=1, pady=1)

        # Quit Button - Exit the application
        self.quitButton = Button(self.frame, text="Quit", font=("Arial BOLD", 11), fg='black', bg='PaleVioletRed2',
                           height=1, width=25, command=self.quit)
        self.quitButton.grid(row=8, column=1, padx=1, pady=1)

    
    # ---------- CLASS FUNCTIONS ------------ #

    def switch_welcome(self):
        # self.frame.forget()
        Welcome.Welcome(self.gui,self.userName.get()).rais()
        self.frame.destroy()

    def switch(self):
        # self.frame.forget()
        SignUp.SignUp(self.gui).rais()
        self.frame.destroy()

    def rais(self):
        self.frame.tkraise()

    def reset(self):
        self.password.delete(0,"end")
        self.userName.delete(0,"end")
        self.label_auth.config(text="")

    def sign_in(self):
        username_check = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", self.userName.get())
        password_check = re.search("[^\\s]{8,}", self.password.get())
        if not username_check or not password_check:
            print("Invalid username or password")

            self.label_auth.config(text="Invalid username or password")

            return False
        # hashpass = self.hash_password(
        #     self.password.get())
        if db.signin(self.userName.get(), self.password.get(), self.label_auth):

            self.switch_welcome()

    def hash_password(self,password):
        hashed_password = generate_password_hash(password)
        return hashed_password
    
    def quit(self):
        self.gui.quit()


if __name__ == "__main__":
    guii = Tk()
    guii.geometry("800x500")


    # start the GUI
    win = SignIn(guii)
    guii.mainloop()