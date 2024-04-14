# Author: Nusaiba Mahmood
# File: Screen_01_SignIn.py

# import everything from tkinter module 
from tkinter import *

# Driver code 
if __name__ == "__main__":
    # create a GUI window 
    gui = Tk()

    # set the background colour of GUI window 
    gui.configure(background="#404040")

    # aligns widgets by weighting rows and columns
    gui.columnconfigure((0,2), weight=1, uniform="anything")
    gui.rowconfigure((0,8), weight=1, uniform="anything")

    # set the title of GUI window 
    gui.title("SKYN Emotion Detection Music Player") 

    # set the configuration of GUI window 
    gui.geometry("800x500")

    welcomeLabel = Label(gui, text=" Sign In ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
    welcomeLabel.grid(row=0, column=1, padx=5, pady=5, sticky="s")

    usernameLabel = Label(gui, text = "Username:", fg="white", bg="#404040", font=("Arial BOLD", 12))
    usernameLabel.grid(row=2, column=0, pady=1, padx=1, sticky="e")
    userName = Entry(gui, width=30)
    userName.grid(row=2, column=1, pady=3)

    passwordLabel = Label(gui, text = "Password:", fg="white", bg="#404040", font=("Arial BOLD", 12))
    passwordLabel.grid(row=4, column=0, pady=1, padx=1, sticky="e")
    password = Entry(gui, width=30)
    password.grid(row=4, column=1, pady=3)
        
    # create buttons and place at a particular 
    # location inside the root window 
    # when user press the button, the command or
    # function affiliated to that button is executed

    signInButton = Button(gui, text=' Sign In ', font=("Arial BOLD", 11),fg='black', bg='light blue', height=1, width=20)
    signInButton.grid(row=6, column=1, pady=1)
    
    signUpButton = Button(gui, text=' Sign Up ', font=("Arial BOLD", 11), fg='black', bg='light goldenrod', height=1, width=20)
    signUpButton.grid(row=7, column=1, pady=1)
        
    # start the GUI
    gui.mainloop()