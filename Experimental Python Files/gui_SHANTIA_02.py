import tkinter as tk
import random
import pygame

pygame.init()


class GUI(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Team SKYN Emotion Detection Music Player")
       self.geometry("400x300")

       self.frames = {}
       for ScreenClass in [WelcomeScreen, EmotionDetectionScreen, MusicPlayerScreen]:
           frame = ScreenClass(self)
           self.frames[ScreenClass] = frame
           frame.grid(row=5, column=10, sticky="nsew")

       self.show_screen(WelcomeScreen)

       self.buttons_frame = tk.Frame(self)
       self.buttons_frame.grid(row=1, column=10, sticky="ew")

       button_names = ["Welcome", "Emotion Detection", "Music Player"]
       for idx, (ScreenClass, button_name) in enumerate(zip([WelcomeScreen, EmotionDetectionScreen, MusicPlayerScreen],
                                                            button_names)):
           button = tk.Button(self.buttons_frame, text=button_name,
                              command=lambda s=ScreenClass: self.show_screen(s))
           button.grid(row=0, column=idx, sticky="ew")

   def show_screen(self, screenclass):
       frame = self.frames[screenclass]
       frame.tkraise()


class WelcomeScreen(tk.Frame):
   def __init__(self, parent):
       super().__init__(parent)
       label_welcome = tk.Label(self, text="Welcome to SKYN Emotion Detection Music Player")
       label_welcome.pack()


class EmotionDetectionScreen(tk.Frame):
   def __init__(self, parent):
       super().__init__(parent)
       label_emotion = tk.Label(self, text="Choose your emotion:")
       label_emotion.pack()

       emotions = ['happy', 'stress', 'focus', 'fear']
       for emotion in emotions:
           button = tk.Button(self, text=emotion.capitalize(),
                              command=lambda e=emotion: self.detect_emotion(e))
           button.pack()

   def detect_emotion(self, emotion):
       if emotion in music_library:
           print("Emotion detected:", emotion)
           playlist = generate_playlist(emotion)
           if playlist:
               print("Generated playlist for", emotion + ":")
               for song in playlist:
                   print(song)

               self.master.show_screen(MusicPlayerScreen)
               self.master.frames[MusicPlayerScreen].update_playlist(playlist)
           else:
               print("No playlist generated.")
       else:
           print("Emotion not recognized.")


class MusicPlayerScreen(tk.Frame):
   def __init__(self, parent):
       super().__init__(parent)

       self.label_playlist = tk.Label(self, text="Music Player")
       self.label_playlist.pack()

       self.playlist = []  # Initialize as a list

       self.play_button = tk.Button(self, text="Play", command=self.play_music)
       self.play_button.pack(side=tk.LEFT)

       self.pause_button = tk.Button(self, text="Pause", command=self.pause_music)
       self.pause_button.pack(side=tk.LEFT)

       self.stop_button = tk.Button(self, text="Stop", command=self.stop_music)
       self.stop_button.pack(side=tk.LEFT)

       self.volume_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume",
                                    command=self.set_volume)
       self.volume_scale.pack()

       self.canvas = tk.Canvas(self, width=300, height=40, bg="black")
       self.canvas.pack()

       self.draw_music_bar()

       self.song_index = None

       self.mood_var = tk.StringVar(self)
       self.mood_var.set("Select Mood")

       def mood_changed():
           selected_mood = self.mood_var.get()
           if selected_mood in music_library:
               self.playlist = music_library[selected_mood]
           else:
               self.playlist = []

       self.mood_menu = tk.OptionMenu(self, self.mood_var, *music_library.keys())
       self.mood_menu.pack()
       self.mood_var.trace("w", mood_changed)

   def draw_music_bar(self):
       self.canvas.delete("all")

       bar_width = 200
       bar_height = 20
       bar_color = "light blue"
       self.canvas.create_rectangle(50, 5, 50 + bar_width, 5 + bar_height, fill=bar_color)

   def play_music(self):
       selected_song = random.choice(self.playlist)  # Select a random song from the playlist
       print("Playing:", selected_song)

       try:
           pygame.mixer.music.load(selected_song)
           pygame.mixer.music.play()
       except pygame.error as e:
           print("Error:", e)

   def update_playlist(self, playlist):
       self.playlist = playlist  # Update the playlist
       self.playlist.delete(0, tk.END)
       for song in playlist:
           self.playlist.insert(tk.END, song)

   def pause_music(self):
       pygame.mixer.music.pause()
       print("Pausing music")
       self.pause_music()

   def stop_music(self):
       pygame.mixer.music.stop()
       print("Stopping music")
       self.song_index = None

   def set_volume(self, volume):
       pygame.mixer.music.set_volume(float(volume) / 100)
       print("Volume set to", volume)
       self.set_volume(100)


music_library = {
   'happy': ['HappySong1.mp3', 'HappySong2.mp3', 'HappySong3.mp3'],
   'stress': ['StressSong1.mp3', 'StressSong2.mp3', 'StressSong3.mp3'],
   'focus': ['FocusSong1.mp3', 'FocusSong2.mp3', 'FocusSong3.mp3']
}


def generate_playlist(emotion):
   if emotion in music_library:
       playlist = music_library[emotion]
       random.shuffle(playlist)
       return playlist
   else:
       return []


if __name__ == "__main__":
   app = GUI()
   app.mainloop()

