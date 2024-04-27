# Author: Nusaiba Mahmood, Kwame Addo
# File: AddMusic.py

import SignIn
import Welcome

# import everything from tkinter module
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
import shutil


class AddMusic:
    # ---------- GUI Init Function --------- #
    def __init__(self, gui, name):
        self.name = name
        self.gui = gui
        self.bg = PhotoImage(file="./Assets/Images/music-sikaku4.png")
        self.frame = Label(gui, image=self.bg)
        self.gui.attributes('-fullscreen', True)

        # GUI Grid configurations
        self.frame.columnconfigure((0, 4), weight=1, uniform="anything")
        self.frame.configure(background="#404040", width=800, height=500)

        self.frame.rowconfigure((0, 6), weight=1, uniform="anything")
        self.frame.pack(fill='both', expand=True)

        # ADD MUSIC! Page Title
        self.addMusicLabel = Label(self.frame, text=f"ADD MUSIC!", fg="white", bg="#404040", font=("Consolas BOLD", 30))
        self.addMusicLabel.grid(row=0, column=2)

        # Create and place buttons in the root window.
        # The function in the command attribute is executed when the button is clicked.
        
        # + ANGER MUSIC Button
        self.addAnger = Button(self.frame, text=' ➕ ANGER MUSIC ',
                               font=("Arial BOLD", 11),
                               fg='black', bg='LightSalmon2', height=10, width=25, padx=2, pady=2
                               ,command=lambda: self.add_music('anger'))
        self.addAnger.grid(row=1, column=1)

        # + DISGUST MUSIC Button
        self.addDisgust = Button(self.frame, text=' ➕ DISGUST MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='DarkOliveGreen2', height=10, width=25, padx=2, pady=2
                                ,command=lambda: self.add_music('disgust'))
        self.addDisgust.grid(row=1, column=2)

        # + HAPPINESS MUSIC Button        
        self.addHappiness = Button(self.frame, text=' ➕ HAPPINESS MUSIC ',
                                   font=("Arial BOLD", 11),
                                   fg='black', bg='gold', height=10, width=25, padx=2, pady=2
                                   ,command=lambda: self.add_music('happiness'))
        self.addHappiness.grid(row=3, column=1)

        # + NEUTRAL MUSIC Button
        self.addNeutral = Button(self.frame, text=' ➕ NEUTRAL MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='bisque', height=10, width=25, padx=2, pady=2
                                 ,command=lambda: self.add_music('neutral'))
        self.addNeutral.grid(row=3, column=2)

        # + SADNESS MUSIC Button
        self.addSadness = Button(self.frame, text=' ➕ SADNESS MUSIC ',
                                 font=("Arial BOLD", 11),
                                 fg='black', bg='cornflower blue', height=10, width=25, padx=2, pady=2
                                 ,command=lambda: self.add_music('sadness'))
        self.addSadness.grid(row=3, column=3)

        # + SURPRISE MUSIC Button
        self.addSurprise = Button(self.frame, text=' ➕ SURPRISE MUSIC ',
                                  font=("Arial BOLD", 11),
                                  fg='black', bg='VioletRed1', height=10, width=25, padx=2, pady=2
                                  ,command=lambda: self.add_music('surprise'))
        self.addSurprise.grid(row=5, column=2)

        # + FEAR MUSIC Button
        self.addFear = Button(self.frame, text=' ➕ FEAR MUSIC ',
                              font=("Arial BOLD", 11),
                              fg='black', bg='ghost white', height=10, width=25, padx=2, pady=2
                              ,command=lambda: self.add_music('fear'))
        self.addFear.grid(row=5, column=3)

        # SIGN OUT Button to sign out of the application and switch to Sign In screen in SignIn.py file 
        self.signOutButton = Button(self.frame, text="↪ SIGN OUT", font=("Arial BOLD", 12), fg='black',
                           bg='MediumPurple1', height=10, width=25, padx=2, pady=2, command=self.reset)
        self.signOutButton.grid(row=6, column=4)

        # BACK Button - Return to previous screen in Welcome.py
        self.backButton = Button(self.frame, text="🔙 BACK", font=("Arial BOLD", 12), fg='black',
                                  bg='MediumPurple1', height=10, width=25, padx=2, pady=2, command=self.back_welcome)
        self.backButton.grid(row=6, column=0)

    # ---------- CLASS FUNCTIONS ------------ #

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


# if __name__ == "__main__":
#     app = Tk()
#     #AddMusic(app, "Kwame")
#     app.mainloop()
