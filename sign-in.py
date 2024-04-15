import tkinter
import sqlite3
import re
from werkzeug.security import generate_password_hash,check_password_hash

window = tkinter.Tk()
window.geometry('340x440')
window.configure(bg='#333333')
frame = tkinter.Frame(bg='#333333')

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
def hash_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password
def signup():
    x = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", username_input.get())
    p = re.search("[^\\s]{8,}", password_entry.get())
    if x == None or p == None:
        print("Invalid username or password")
        return False
    hashpass = hash_password(password_entry.get())
    # Insert username and password into the table
    try:
        c.execute("INSERT INTO signUp (username, password) VALUES (?, ?)", (username_input.get(), hashpass))
        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Sign up successful")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists")
        return False
def signin(name, password):
    x = re.search("^[A-Za-z][A-Za-z0-9]{4,10}$", name)
    p = re.search("[^\\s]{8,}", password)
    if x is None or p is None:
        print("Invalid username or password")
        return False
    # hashpass = hash_password(password)
    con = sqlite3.connect("mydatabase.db")
    check = f"SELECT * FROM signUp WHERE username='{name}'"
    output = con.execute(check)
    result = output.fetchone()
    con.close()

    if result is None or not check_password_hash(result[1], password):
        print("Username or password does not exist")
        return False
    else:
        print(f"Hello there, {name}!")
        open_next_window()
        return True

def open_next_window():
    # Close the current window
    window.destroy()
    # Execute code from another file
    with open('expression_ssd_detect.py', 'r') as file:
        exec(file.read())


#creating widgets
login_label = tkinter.Label(frame, text="Welcome back! ", bg='#333333', fg='#fff', font=("Arial",30))
username_label= tkinter.Label(
frame,text ="Username",bg='#333333', fg="#fff",font=("Arial",16))
username_input = tkinter.Entry(frame,font=("Arial",16))
password_entry= tkinter.Entry(frame,show ="*",font=("Arial",16))
password_label= tkinter.Label(
frame,text ="Password",bg='#333333',fg='#fff',font=("Arial",16))


login_button = tkinter.Button(frame, text="Login", bg="#005A9C",fg="#000",font=("Arial",16), command=lambda: signin(username_input.get(), password_entry.get()))
signUp_button = tkinter.Button(frame, text="Sign Up", bg="#005A9C",fg="#000",font=("Arial",16), command=signup)

#placing widgets
login_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_input.grid(row=1, column=1,pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)
signUp_button.grid(row=4,column=0,columnspan=2,pady=30)
frame.pack()

#it implies the end of the page, any line of code after the mainloop() method will not run
window.mainloop()