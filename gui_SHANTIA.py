import tkinter as tk

def button_click():
   label.config(text="Button clicked!")


root = tk.Tk()
root.title("SKYN Emotion Detection Music Player")

root.configure(bg="black")

label = tk.Label(root, text="Hello, User!")
label.pack()


button = tk.Button(root, text="Sign-in", command=button_click)
button.pack()

root.mainloop() 

def select_music(mood):
   if mood == "happy":
       return "hip hop"
   elif mood == "sad":
       return "nature sounds"
   elif mood == "angry":
       return "acoustic guitar"
   elif mood == "calm":
       return "classical"
   else:
       return "meditation"

mood = input("Enter your mood: ")
selected_music = select_music(mood.lower())
print("Recommended music genre:", selected_music)

def play_music():
   emotion = entry_emotion.get()

   # Example: if emotion == "sad":
   #             play_relief_music()
   #          elif emotion == "happy":
   #             play_motivated_music()
   #          else:
   #             play_focus_music()


root = tk.Tk()
root.title("Emotion Detection Music Player")

("Changing GUI Background Color")
root.configure(bg="gray")

label_emotion = tk.Label(root, text="Enter your emotion:")
label_emotion.pack()

entry_emotion = tk.Entry(root)
entry_emotion.pack()

button_play = tk.Button(root, text="Play Music", command=play_music)
button_play.pack()

root.main()


