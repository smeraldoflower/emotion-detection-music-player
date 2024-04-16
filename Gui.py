from tkinter import *
# Driver code
# if __name__ == "__main__":
#     # create a GUI window

if __name__ == "__main__":
    gui = Tk()
    def guispawn():


    # set the background colour of GUI window
    # gui.configure(background="#404040")

    # aligns widgets by weighting rows and columns
    # gui.columnconfigure((0, 2), weight=1, uniform="anything")
    # gui.rowconfigure((0, 8), weight=1, uniform="anything")

    # set the title of GUI window
        gui.title("SKYN Emotion Detection Music Player")

    # set the configuration of GUI window
        gui.geometry("800x500")
        return gui

    def run():
        gui.mainloop()