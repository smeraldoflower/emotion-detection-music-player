import tkinter
from tkinter import *
from tkinter import filedialog
import os
import pygame

# pygame.mixer.init()
class Window:
    def __init__(self, master,mood = None):
        self.mood = mood
        self.play_img  = PhotoImage(file="play.png")

        self.prev_img  = PhotoImage(file="previous.png")

        self.next_img = PhotoImage(file="next(1).png")

        self.pause_img = PhotoImage(file="pause.png")

        self.frame = Frame(master)
        self.frame_bottom = Frame(self.frame)

        self.play_button = Button(self.frame_bottom,  text="",command=self.play_music,borderwidth=0,image=self.play_img)

        self.prev_button = Button(self.frame_bottom,  text="",command=self.prev_music,borderwidth=0,image=self.prev_img)

        self.next_button = Button(self.frame_bottom,  text="",command=self.next_music,borderwidth=0,image=self.next_img)

        self.pause_button = Button(self.frame_bottom, text="",command=self.pause_music,borderwidth=0,image=self.pause_img)


        self.song_list = Listbox(self.frame,bg="black", fg="white", width=100,height=15)

        self.song_list.pack(fill="both",expand=True)

        self.frame.grid(row=0,column=0,sticky=tkinter.NSEW) # restore
        # self.frame.pack()
        self.frame.tkraise()
        pygame.mixer.init()

        self.frame_bottom.pack()
        self.play_button.grid(row=0,column=1, padx= 7,pady= 10)
        self.prev_button.grid(row=0,column=0, padx= 7,pady= 10)
        self.pause_button.grid(row=0,column=2, padx= 7,pady= 10)
        self.next_button.grid(row=0,column=3, padx= 7,pady= 10)

        # self.play_button.grid(row=0,column=0)
        # self.pause_button.pack()

        self.menu = Menu(master)

        self.songs = []

        self.pause = False

        master.config(menu=self.menu)

        self.menu_bar = Menu(self.menu,tearoff=False)
        self.menu_bar.add_command(label="Select Folder", command = self.load_music)
        self.menu.add_cascade(label="File",menu=self.menu_bar)
        self.current_song = ""
        self.directory = ""

    def load_music(self):
        diag = filedialog.askdirectory()
        # match self.mood:
        #     case "Happiness":
        #         path = "Emotion Music/happiness"
        #         os.chdir(path)
        #     case "anger":
        #         path = "Emotion Music/anger"
        #
        #         os.chdir(path)
        #     case "anger":
        #         path = "Emotion Music/anger"
        #
        #         os.chdir(path)
        #     case "anger":
        #         path = "Emotion Music/anger"
        #
        #         os.chdir(path)

        # diag = os.getcwd()
        self.directory = diag
        for song in os.listdir(diag):
            name, ext = os.path.splitext(song)
            if ext == ".mp3":
                self.songs.append(song)
        print(self.directory)

        for song in self.songs:
            self.song_list.insert("end",song)
        self.song_list.select_set(0)
        self.current_song = self.songs[self.song_list.curselection()[0]]

    def print_song(self):
        print(self.mood)

    def play_music(self,next_check= True):
        if next_check:
            self.current_song = self.songs[self.song_list.curselection()[0]]
        if not self.pause:
            # print(os.path.join(self.directory, self.current_song))
            pla = os.path.join(self.directory, self.current_song)
            pla = pla.replace("\\","/")
            # print(pla)
            self.print_song()
            pygame.mixer.music.load(pla)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
            self.pause = False

    def pause_music(self):
        pygame.mixer.music.pause()
        self.pause = False

    def next_music(self):
        if self.song_list.curselection()[0] == len(self.songs) -1:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(0)
            self.current_song = self.songs[0]
            self.play_music(False)
        else:
            self.song_list.select_clear(0,END)
            self.song_list.select_set(self.songs.index(self.current_song)+1)
            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)

    def prev_music(self):
        if self.song_list.curselection()[0] == 0:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(len(self.songs)-1)
            self.current_song = self.songs[len(self.songs)-1]
            self.play_music(False)
        else:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(self.songs.index(self.current_song) - 1)
            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)

        # print(self.song_list.curselection()[0])

            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)
