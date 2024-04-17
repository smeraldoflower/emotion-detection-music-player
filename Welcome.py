# Author: Nusaiba Mahmood
# File: Screen_02_Welcome_User.py

# import everything from tkinter module
from tkinter import *
from tkinter import filedialog
import SignIn
import EmotionDetection
import AddMusic


# import EmotionDetection
#
# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     gui = Tk()
#
#     # set the background colour of GUI window
#     gui.configure(background="#404040")
#
#     # aligns widgets by weighting rows and columns
#     gui.columnconfigure((0, 2), weight=1, uniform="anything")
#     gui.rowconfigure((0, 4), weight=1, uniform="anything")
#
#     # set the title of GUI window
#     gui.title("SKYN Emotion Detection Music Player")
#
#     # set the configuration of GUI window
#     gui.geometry("800x500")
class Welcome:
    def __init__(self, gui,name):
        self.name = name
        self.gui = gui
        self.frame = Frame(self.gui)
        self.gui.attributes('-fullscreen', True)

        self.welcomeLabel = Label(self.frame, text=f" WELCOME {self.name}! ", fg="white", bg="#404040",
                                  font=("Consolas BOLD", 30))
        self.welcomeLabel.grid(row=0, column=1)

        # create buttons and place at a particular
        # location inside the root window
        # when user press the button, the command or
        # function affiliated to that button is executed
        self.button1 = Button(self.frame, text=' ➕ ADD MUSIC DIRECTORY ', 
                              font=("Arial BOLD", 11),
                              fg='black', bg='white', height=10, width=25,
                              command=self.switch_addMusic)
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.frame, text=' 🎵 DETECT EMOTION ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='light blue', height=10, width=25,
                              command=self.successful)
        self.button2.grid(row=2, column=1)

        self.button3 = Button(self.frame, text=' ↪ SIGN OUT ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='pink', height=10, width=25,
                              command=self.reset)
        self.button3.grid(row=2, column=2)
        # set the background colour of GUI window

        # aligns widgets by weighting rows and columns
        self.frame.columnconfigure((0, 2), weight=1, uniform="anything")
        self.frame.configure(background="#404040", width=800, height=500)

        self.frame.rowconfigure((0, 4), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

        self.frame.pack()

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

if __name__ == "__main__":
    pass
        # start the GUI

    # app = Tk()
    # gui = Welcome(app)
    # app.mainloop()