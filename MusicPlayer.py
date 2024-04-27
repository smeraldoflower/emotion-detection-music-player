# Author: Kwame Addo
# File: Music_player.py

# import everything from tkinter module

import tkinter
from tkinter import *

import os
import pygame

import EmotionDetection


class Window:
    def __init__(self, master, mood=None):
        self.master = master
        self.mood = mood
        # self.play_img = PhotoImage(file="play.png")

        # self.prev_img = PhotoImage(file="previous.png")

        # self.next_img = PhotoImage(file="next(1).png")

        # self.pause_img = PhotoImage(file="pause.png")

        self.frame = Frame(self.master, bg="#404040")

        self.master.geometry("640x480")
        self.master.attributes("-fullscreen", True)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.frame_bottom = Frame(self.frame, bg="#404040")

        self.play_button = Button(self.frame_bottom, text="▶", command=self.play_music,
                                  borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")

        self.prev_button = Button(self.frame_bottom, text="⏮", command=self.prev_music,
                                  borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")

        self.next_button = Button(self.frame_bottom, text="⏭", command=self.next_music,
                                  borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")
        self.close_button = Button(self.frame_bottom, text="👋 Quit", command=self.quit,
                                   borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")

        self.back_button = Button(self.frame_bottom, text="🔙 Back", command=self.back,
                                    borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")

        self.pause_button = Button(self.frame_bottom, text="⏸", command=self.pause_music,
                                   borderwidth=0, font=("Arial BOLD", 40), bg="#404040", fg="white")

        self.song_list = Listbox(self.frame, bg="black", fg="white", width=100, height=15, font=("Consolas BOLD", 25))

        self.song_list.pack(fill="both", expand=True)

        self.frame.grid(row=0, column=0, sticky=tkinter.NSEW)  # restore
        # self.frame.pack()
        self.frame.tkraise()
        pygame.mixer.init()

        self.frame_bottom.pack()
        self.play_button.grid(row=0, column=1, padx=7, pady=10)
        self.prev_button.grid(row=0, column=0, padx=7, pady=10)
        self.pause_button.grid(row=0, column=2, padx=7, pady=10)
        self.next_button.grid(row=0, column=3, padx=7, pady=10)
        self.close_button.grid(row=0, column=5,padx =7, pady=10, sticky="ws")
        self.back_button.grid(row=0, column=4, padx=7, pady=10, sticky="ws")

        # self.play_button.grid(row=0,column=0)
        # self.pause_button.pack()

        # self.menu = Menu(master)

        self.songs = []

        self.pause = False

        self.current_song = ""
        self.directory = ""
        self.load_music()
        self.play_music()

    def load_music(self):
        # music_dir = filedialog.askdirectory()
        match self.mood:
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
            case "neutral":
                path = "Emotion/neutral"

                os.chdir(path)
            case "surprise":
                path = "Emotion/surprise"

                os.chdir(path)
            case "anger":
                path = "Emotion/surprise"

                os.chdir(path)

        # get the directory containing the mood detected from the camera
        music_dir: str = os.getcwd()

        # cd directory twice to make sure we static files can be referenced
        os.chdir(os.path.dirname(os.getcwd()))
        os.chdir(os.path.dirname(os.getcwd()))

        print(os.getcwd())
        self.directory = music_dir
        for song in os.listdir(music_dir):
            """Loops to feel up the songs from the directory to the songs array"""
            name, ext = os.path.splitext(song)
            if ext == ".mp3":
                self.songs.append(song)
        print(self.directory)

        # Songs are now added to the Tkinter ListBox
        for song in self.songs:
            self.song_list.insert("end", song)
        self.song_list.select_set(0)
        try:
            self.current_song = self.songs[self.song_list.curselection()[0]]
            print(f" here is the cwd ----{os.getcwd()}")
        except:
            print("No music")
        finally:
            print("done")

    def print_song(self):
        print(self.mood)

    def quit(self):
        self.master.quit()

    def play_music(self, next_check=True) -> None:
        """ Play music function"""
        if next_check:
            self.current_song = self.songs[self.song_list.curselection()[0]]
        if not self.pause:
            # print(os.path.join(self.directory, self.current_song))
            pla = os.path.join(self.directory, self.current_song)
            pla = pla.replace("\\", "/")
            # print(pla)
            self.print_song()
            pygame.mixer.music.load(pla)
            pygame.mixer.music.play()
            self.play_button.configure(bg="#556B2F",highlightbackground="red")
            self.pause_button.configure(bg="#404040", highlightbackground="red")

        else:
            pygame.mixer.music.unpause()
            # self.play_button.configure(bg="#404040", highlightbackground="red")
            self.play_button.configure(bg="#556B2F",highlightbackground="red")

            self.pause = False

    def pause_music(self) -> None:
        """Setting function for the pause. This causes the music to stop when pause is set to false"""
        pygame.mixer.music.pause()
        self.pause_button.configure(bg="#556B2F", highlightbackground="red")
        self.play_button.configure(bg="#404040", highlightbackground="red")

        self.pause = False

    def next_music(self) -> None:
        """ Skip to the next song"""
        if self.song_list.curselection()[0] == len(self.songs) - 1:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(0)
            self.current_song = self.songs[0]
            self.play_music(False)
        else:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(self.songs.index(self.current_song) + 1)
            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)

    def prev_music(self) -> None:
        """ Previous song function"""
        if self.song_list.curselection()[0] == 0:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(len(self.songs) - 1)
            self.current_song = self.songs[len(self.songs) - 1]
            self.play_music(False)
        else:
            self.song_list.select_clear(0, END)
            self.song_list.select_set(self.songs.index(self.current_song) - 1)
            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)

            # print(self.song_list.curselection()[0])

            self.current_song = self.songs[self.song_list.curselection()[0]]
            self.play_music(False)

    def back(self):
        pygame.mixer.quit()
        self.frame.destroy()
        EmotionDetection.Emotion(self.master)


if __name__ == "__main__":
    app = Tk()
    Window(app, "Kwame")
    app.mainloop()
