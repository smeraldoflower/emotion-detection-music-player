from tkinter import *
from PIL import Image, ImageTk
import Music_player


class Frame_gui:
    def __init__(self, frame, app, pack=False):
        self.frame = frame
        self.app = app
        self.pack = pack
        self.container = Frame()
        # self.captured_img = Image.fromarray(frame)
        # self.photo = ImageTk.PhotoImage(self.captured_img)
        # self.label = Label(app, image=self.photo)
        # self.label.image = self.photo
        # self.set_pack(pack)
        self.captured_img = None
        self.photo = None
        self.label = None

        self.run(self.frame)
        self.set_pack(self.pack)

    def set_pack(self, pack):
        if pack:

            self.label.grid(row=0, column=0)

    def setRaise(self, pack):
        if pack:
            self.label.destroy()


    def run(self,frame):
        if frame is not None:
            self.captured_img = Image.fromarray(self.frame)
            self.photo = ImageTk.PhotoImage(self.captured_img)
            self.label = Label(self.app, image=self.photo)
            self.label.image = self.photo
            self.set_pack(self.pack)
        else:
            self.setRaise(True)

