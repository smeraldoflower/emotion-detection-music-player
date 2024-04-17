import tkinter
from tkinter import *
from PIL import Image, ImageTk
import MusicPlayer


class Frame_gui:
    def __init__(self, frame , app, pack=False):
        self.frame = frame
        self.app = app
        self.pack = pack
        # self.container = Frame()
        # self.captured_img = Image.fromarray(frame)
        # self.photo = ImageTk.PhotoImage(self.captured_img)
        # self.label = Label(app, image=self.photo)
        # self.label.image = self.photo
        # self.set_pack(pack)
        self.captured_img = None
        self.photo = None
        self.label = Label(self.app, bg="#404040")
        self.label.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.app.attributes('-fullscreen', True)

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.run(self.frame)
        self.set_pack(self.pack)


    def set_pack(self, pack):
        if pack:
            pass
            # self.container.grid(row=0, column=0,sticky=tkinter.NSEW)
            # self.app.geometry("500x500")
            # self.app.geometry("640x520")



    def setRaise(self, pack):
        if pack:
            self.label.destroy()


    def run(self,frame):

        if frame is not None:
            self.captured_img = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(self.captured_img)
            self.label.image = self.photo
            self.label.configure(image=self.photo)
            self.set_pack(self.pack)
        else:
            print(":E")
            # self.setRaise(True)

