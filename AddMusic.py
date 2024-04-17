# Author: Nusaiba Mahmood
# File: Screen_02_Welcome_User.py

# import everything from tkinter module
from tkinter import *
from tkinter import filedialog
import os

import SignIn
import EmotionDetection
import Welcome


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
class AddMusic:
    def __init__(self, gui):
        self.gui = gui
        self.frame = Frame(gui)
        self.gui.attributes('-fullscreen', True)

        self.AddLabel = Label(self.frame, text=f"ADD", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.AddLabel.grid(row=0, column=1, sticky='e')

        self.MusicLabel = Label(self.frame, text=f"MUSIC!", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.MusicLabel.grid(row=0, column=2, sticky='w')

        # create buttons and place at a particular
        # location inside the root window
        # when user press the button, the command or
        # function affiliated to that button is executed
        self.addAnger = Button(self.frame, text=' ➕ ANGER MUSIC ',
                               font=("Arial BOLD", 11),
                               fg='black', bg='LightSalmon2', height=10, width=25, padx=2, pady=2
                               ,command=lambda: self.add_music('anger'))
        self.addAnger.grid(row=1, column=0)

        self.addDisgust = Button(self.frame, text=' ➕ DISGUST MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='DarkOliveGreen2', height=10, width=25, padx=2, pady=2
                                ,command=lambda: self.add_music('disgust'))
        self.addDisgust.grid(row=1, column=1)

        self.addFear = Button(self.frame, text=' ➕ FEAR MUSIC ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='ghost white', height=10, width=25, padx=2, pady=2
                              ,command=lambda: self.add_music('fear'))
        self.addFear.grid(row=1, column=2)

        self.addHappiness = Button(self.frame, text=' ➕ HAPPINESS MUSIC ',
                                   font=("Arial BOLD", 11),
                                   fg='black', bg='gold', height=10, width=25, padx=2, pady=2
                                   ,command=lambda: self.add_music('happiness'))
        self.addHappiness.grid(row=3, column=0)

        self.addNeutral = Button(self.frame, text=' ➕ NEUTRAL MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='bisque', height=10, width=25, padx=2, pady=2
                                 ,command=lambda: self.add_music('neutral'))
        self.addNeutral.grid(row=3, column=1)

        self.addSadness = Button(self.frame, text=' ➕ SADNESS MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='cornflower blue', height=10, width=25, padx=2, pady=2
                                 ,command=lambda: self.add_music('sadness'))
        self.addSadness.grid(row=3, column=2)

        self.addSurprise = Button(self.frame, text=' ➕ SURPRISE MUSIC ',
                                  font=("Arial BOLD", 11),
                                  fg='black', bg='VioletRed1', height=10, width=25, padx=2, pady=2
                                  ,command=lambda: self.add_music('surprise'))
        self.addSurprise.grid(row=5, column=1)         
        
        # set the background colour of GUI window

        # aligns widgets by weighting rows and columns
        self.frame.columnconfigure((0, 4), weight=1, uniform="anything")
        self.frame.configure(background="#404040", width=800, height=500)

        self.frame.rowconfigure((0, 6), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

        self.frame.pack()

    def switch(self):
        # self.frame.forget()
        # SignUp.SignUp(self.gui).rais()
        self.frame.destroy()

    def reset(self):
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()

    def rais(self):
        self.frame.tkraise()

    def add_music(self, dir):
    # music_dir = filedialog.askdirectory()
        match dir:
            case "happiness":
                path = "Emotion/happiness"
                os.chdir(path)
            case "disgust":
                path = "Emotion/disgust"
                os.chdir(path)
            case "fear":
                path = "Emotion/fear"
                os.chdir(path)
            case "sadness":
                path = "Emotion/sadness"
                os.chdir(path)
            case  "neutral":
                path = "Emotion/neutral"
                os.chdir(path)
            case "surprise":
                path = "Emotion/surprise"
                os.chdir(path)
            case "anger":
                path = "Emotion/anger"
                os.chdir(path)
                print(os.getcwd())

        directory = filedialog.askopenfilename()

        print(directory)

if __name__ == "__main__":
    pass
        # start the GUI

    # app = Tk()
    # gui = Welcome(app)
    # app.mainloop()