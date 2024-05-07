# Author: Nusaiba Mahmood, Kwame Addo
# File: Welcome.py

import SignIn as SignIn
import EmotionDetection as EmotionDetection
import AddMusic as AddMusic

# import everything from tkinter module
from tkinter import *
from tkinter import filedialog

class Welcome:
    # ---------- GUI Init Function --------- #
    def __init__(self, gui,name):
        self.name = name
        self.gui = gui
        self.bg = PhotoImage(file="./Assets/Images/music-sikaku4.png")
        self.frame = Label(gui, image=self.bg)
        #self.frame = Frame(self.gui)
        self.gui.attributes('-fullscreen', True)

        # GUI Grid configurations
        self.frame.columnconfigure((0, 2), weight=1, uniform="anything")
        self.frame.configure(background="#404040", width=800, height=500)

        self.frame.rowconfigure((0, 4), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

        self.frame.pack()

        # Welcome <username> ! Page Title
        self.welcomeLabel = Label(self.frame, text=f" WELCOME {self.name} ! ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.welcomeLabel.grid(row=0, column=1)

        # Create and place buttons in the root window.
        # The function in the command attribute is executed when the button is clicked.

        # ADD MUSIC Button to switch to Add Music screen in AddMusic.py file
        self.addMusicButton = Button(self.frame, text=' ➕ ADD MUSIC ', 
                              font=("Arial BOLD", 11),
                              fg='black', bg='white', height=10, width=25,
                              command=self.switch_addMusic)
        self.addMusicButton.grid(row=2, column=0)

        # DETECT EMOTION Button to switch to Emotion Detection screen in EmotionDetection.py file 
        self.detectEmotionButton = Button(self.frame, text=' 🎵 DETECT EMOTION ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='light blue', height=10, width=25,
                              command=self.successful)
        self.detectEmotionButton.grid(row=2, column=1)

        # SIGN OUT Button to sign out of the application and switch to Sign In screen in SignIn.py file 
        self.signOutButton = Button(self.frame, text=' ↪ SIGN OUT ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='pink', height=10, width=25,
                              command=self.reset)
        self.signOutButton.grid(row=2, column=2)
    
    # ---------- CLASS FUNCTIONS ------------ #

    def switch_addMusic(self):
        # self.frame.forget()
        AddMusic.AddMusic(self.gui,self.name).rais()
        self.frame.destroy()
            
    def switch(self):
        # self.frame.forget()
        # SignUp.SignUp(self.gui).rais()
        self.frame.destroy()

    def reset(self):
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()

    # def successful(self):
    #     EmotionDetection.Emotion(self.gui)
    #     self.frame.destroy()

    def rais(self):
        self.frame.tkraise()

    def add_music(self):
        directory = filedialog.askdirectory()
    def successful(self):
        self.frame.destroy()
        EmotionDetection.Emotion(self.gui)

# if __name__ == "__main__":
#     # app = Tk()
#     # gui = Welcome(app)
#     # app.mainloop()