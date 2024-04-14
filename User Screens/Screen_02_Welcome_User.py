# Author: Nusaiba Mahmood
# File: Screen_02_Welcome_User.py

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
	gui.rowconfigure((0,4), weight=1, uniform="anything")

	# set the title of GUI window 
	gui.title("SKYN Emotion Detection Music Player") 

	# set the configuration of GUI window 
	gui.geometry("800x500")

	welcomeLabel = Label(gui, text=" WELCOME ROCKY! ", fg="white", bg="#404040", font=("Consolas BOLD", 30))
	welcomeLabel.grid(row=0, column=1)
	
	# create buttons and place at a particular 
	# location inside the root window 
	# when user press the button, the command or
	# function affiliated to that button is executed
	button1 = Button(gui, text=' ➕ ADD MUSIC ', fg='black', bg='white', height=10, width=25) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 🎵 DETECT EMOTION ', fg='black', bg='light blue', height=10, width=25) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' ↪ SIGN OUT ', fg='black', bg='pink', height=10, width=25) 
	button3.grid(row=2, column=2) 
		
	# start the GUI
	gui.mainloop()
