# Authors: Nusaiba Mahmood, Kwame Addo
# File: SignUp.py

import SignIn
import db

import re
from tkinter import *
from tkinter import messagebox
from werkzeug.security import generate_password_hash, check_password_hash


class SignUp:
    def __init__(self, gui):
        #""" User Interface in the constructor function """
        self.gui = gui
        self.frame = Frame(gui)
        
        # self.gui.attributes('-fullscreen', True)
        width = self.gui.winfo_screenwidth()
        height = self.gui.winfo_screenheight()
        
        # setting tkinter window size
        self.gui.geometry("%dx%d" % (width, height))

        # Set the background colour of application's GUI window
        self.frame.configure(background="#404040", width="800", height="500")
        
        # GUI Grid configurations
        self.frame.columnconfigure((0, 2), weight=1, uniform="anything")
        self.frame.rowconfigure((0, 10), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

        # Sign Up Page Title
        self.signUpTitleLabel = Label(self.frame, text=" Sign Up ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.signUpTitleLabel.grid(row=0, column=1, padx=5, pady=5, sticky="s")

        # Invalid Username or Password / Password Mismatch / Username Already Exists Error Text
        self.label_auth = Label(self.frame, text="", fg="VioletRed1", bg="#404040", font=("Arial BOLD ITALIC", 12))
        self.label_auth.grid(row=1,column=1,sticky="n")

        # Create Username: Entry Field
        self.usernameLabel = Label(self.frame, text="Create Username:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.usernameLabel.grid(row=2, column=0, pady=1, padx=1, sticky="e")
        self.userName = Entry(self.frame, width=30, font=("Arial BOLD", 11))
        self.userName.grid(row=2, column=1, pady=3)

        # Create Password: Entry Field
        self.passwordLabel = Label(self.frame, text="Create Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.passwordLabel.grid(row=4, column=0, pady=1, padx=1, sticky="e")
        self.password = Entry(self.frame,show="*", width=30, font=("Arial BOLD", 11))
        self.password.grid(row=4, column=1, pady=3)

        # Re-enter Password: Entry Field
        self.passwordVerLabel = Label(self.frame, text="Re-enter Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
        self.passwordVerLabel.grid(row=5, column=0, pady=1, padx=1, sticky="e")
        self.passwordVer = Entry(self.frame,show="*", width=30, font=("Arial BOLD", 11))
        self.passwordVer.grid(row=5, column=1, pady=3)

        # Blank Divider Label for ui spacing
        self.dividerLabel =Label(self.frame, text="", fg="white", bg="#404040", font=("Consolas BOLD", 11))
        self.dividerLabel.grid(row=6,column=1, pady=3)

        # Create and place buttons in the root window.
        # The function in the command attribute is executed when the button is clicked.

        # Sign Up Button - Switch to Sign In Page in SignIn.py file on successful signup
        self.signUpButton = Button(self.frame, text=' Sign Up ', font=("Arial BOLD", 11), fg='black', bg='light goldenrod',
                                   height=1, width=25, command=self.sign_up)
        self.signUpButton.grid(row=7, column=1, pady=1)

        # Back Button - Return to previous screen in SignIn.py
        self.quitButton = Button(self.frame, text="Back", font=("Arial BOLD", 11), fg='black', bg='light blue',
                           height=1, width=25, command=self.reset)
        self.quitButton.grid(row=8, column=1, padx=1, pady=1)

        # Quit Button - Exit the application
        self.quitButton = Button(self.frame, text="Quit", font=("Arial BOLD", 11), fg='black', bg='PaleVioletRed2',
                           height=1, width=25, command=self.quit)
        self.quitButton.grid(row=9, column=1, padx=1, pady=1)

    # ---------- CLASS FUNCTIONS ------------ #

    def switch(self):
        # self.frame.forget()
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()

    def rais(self):
        self.frame.tkraise()

    def reset(self):
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()
    
    def quit(self):
        self.gui.quit()

    # ------------------------------------------------------------------------------------------------- #
    # ---- Alternative Code Block for showing the sign up error messages using a message box pop-up --- #
    # ------------------------------------------------------------------------------------------------- # 

    # def sign_up(self):
    #     username_check = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", self.userName.get()) # 4-10 characters, Start with alphabet, no spaces, no symbols
    #     password_check = re.search("[^\\s]{8,}", self.password.get()) # minimum 8 characters, no spaces
    #     password_ver = re.search("[^\\s]{8,}", self.passwordVer.get())
    
    #     if not username_check or not password_check:
    #         messagebox.showinfo("Invalid username or password","Username must be 4-10 characters, start with a letter, contain only numbers and letters.\nPassword must be minimum 8 characters, contain no spaces.")
    #         print("Invalid username or password")
    #         return False       
    #     if self.passwordVer.get() != self.password.get():
    #         messagebox.showerror("Password mismatch", "Please re-enter your passwords.")
    #         print("Password mismatch")
    #         return False
    #     hashpass = self.hash_password(
    #         self.password.get())
    #     if db.signup(self.userName.get(), hashpass):
    #         self.switch()
    # ------------------------------------------------------------------------------------------------- #
    # ------------------------------------------------------------------------------------------------- #

    def sign_up(self):
        """ Input validation and account creation """
        username_check = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", self.userName.get())
        password_check = re.search("\\S{8,}", self.password.get())

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
        if db.signup(self.userName.get(), hashpass, self.label_auth):
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
