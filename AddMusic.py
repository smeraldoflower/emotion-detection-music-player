# Author: Nusaiba Mahmood
# File: Screen_02_Welcome_User.py
import shutil
from tkinter import messagebox

# import everything from tkinter module
from tkinter import *
from tkinter import filedialog
import os

import SignIn
import Welcome


# import EmotionDetection

class AddMusic:
    def __init__(self, gui, name):
        self.name = name
        self.gui = gui
        self.bg = PhotoImage(file="Gojo-PNG.png")
        self.frame = Label(gui, image=self.bg)
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
                               fg='black', bg='LightSalmon2', height=10, width=25, padx=2, pady=2,
                               command=lambda: self.add_music('anger'))
        self.addAnger.grid(row=1, column=0)

        self.addDisgust = Button(self.frame, text=' ➕ DISGUST MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='DarkOliveGreen2', height=10, width=25, padx=2, pady=2,
                                 command=lambda: self.add_music('disgust'))
        self.addDisgust.grid(row=1, column=1)

        self.addFear = Button(self.frame, text=' ➕ FEAR MUSIC ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='ghost white', height=10, width=25, padx=2, pady=2,
                              command=lambda: self.add_music('fear'))
        self.addFear.grid(row=1, column=2)

        self.addHappiness = Button(self.frame, text=' ➕ HAPPINESS MUSIC ',
                                   font=("Arial BOLD", 11),
                                   fg='black', bg='gold', height=10, width=25, padx=2, pady=2,
                                   command=lambda: self.add_music('happiness'))
        self.addHappiness.grid(row=3, column=0)

        self.addNeutral = Button(self.frame, text=' ➕ NEUTRAL MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='bisque', height=10, width=25, padx=2, pady=2,
                                 command=lambda: self.add_music('neutral'))
        self.addNeutral.grid(row=3, column=1)

        self.addSadness = Button(self.frame, text=' ➕ SADNESS MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='cornflower blue', height=10, width=25, padx=2, pady=2,
                                 command=lambda: self.add_music('sadness'))
        self.addSadness.grid(row=3, column=3)

        self.addSurprise = Button(self.frame, text=' ➕ SURPRISE MUSIC ',
                                  font=("Arial BOLD", 11),
                                  fg='black', bg='VioletRed1', height=10, width=25, padx=2, pady=2,
                                  command=lambda: self.add_music('surprise'))
        self.addSurprise.grid(row=5, column=3)

        self.quit = Button(self.frame, text="👋 QUIT", font=("Arial BOLD", 30), fg='black',
                           bg='VioletRed1', height=10, width=25, padx=2, pady=2, command=self.quit)

        self.quit.grid(row=6, column=4)

        self.back_button = Button(self.frame, text="🔙 BACK", font=("Arial BOLD", 30), fg='black',
                                  bg='VioletRed1', height=10, width=25, padx=2, pady=2, command=self.back_welcome)

        self.back_button.grid(row=6, column=0)
        # set the background colour of GUI window

        # aligns widgets by weighting rows and columns
        self.frame.columnconfigure((0, 4), weight=1, uniform="anything")
        self.frame.configure(background="#404040", width=800, height=500)

        self.frame.rowconfigure((0, 6), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

    def back_welcome(self):

        Welcome.Welcome(self.gui, self.name).rais()
        self.frame.destroy()

    def switch(self):
        # self.frame.forget()
        # SignUp.SignUp(self.gui).rais()
        self.frame.destroy()

    def reset(self):
        SignIn.SignIn(self.gui).rais()
        self.frame.destroy()

    def rais(self):
        self.frame.tkraise()

    def add_music(self, music):

        match music:
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

        file = filedialog.askopenfilename(title=f"Select Song For {music}",filetypes=[("mp3", "mp3")])

        music_dir: str = os.getcwd()
        print(file)
    # cd directory twice to make sure we static files can be referenced
        os.chdir(os.path.dirname(os.getcwd()))
        os.chdir(os.path.dirname(os.getcwd()))
        print(os.getcwd())
        try:
            shutil.copy(file, music_dir)

            # this takes only the file name and display upon successful upload
            music_name = os.path.splitext(os.path.basename(file))[0]
            messagebox.showinfo("Upload Complete", f"Successfully uploaded {music_name} \n >>>>  {music.upper()} directory")

        except:
            print("Issue")
            return

    def quit(self):
        self.gui.quit()


if __name__ == "__main__":
    app = Tk()
    AddMusic(app, "Kwame")
    app.mainloop()
