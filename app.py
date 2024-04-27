# Author: Team SKYN
# File: app.py

from tkinter import *

import SignIn

if __name__ == "__main__":
    guii = Tk()
    guii.title("Team SKYN Emotion Detection Music Player")
    guii.geometry("800x500")
    guii.bind("<Escape>", lambda e: guii.quit())

    # start the GUI
    win = SignIn.SignIn(guii)
    guii.mainloop()