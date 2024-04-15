# import tkinter
# import sqlite3
# import re
#
# def signup(username, password):
#     x = re.search("^[A-Za-z][A-Za-z0-9]{4,10}$", username)
#     p = re.search("[^\s]{8,}", password)
#     if x is None or p is None:
#         print("Invalid username or password")
#         return False
#
#     con = sqlite3.connect("mydatabase.db")
#     try:
#         inst = f"INSERT INTO signUp VALUES('{username}', '{password}')"
#         con.execute(inst)
#         con.commit()
#         con.close()
#         print("Sign up successful")
#         return True
#     except sqlite3.IntegrityError:
#         print("Username already exists")
#         return False
#
#
# def sign_up():
#     name = username_input.get()
#     password = password_entry.get()
#     if signup(name, password):
#         # Clear input fields after successful sign-up
#         username_input.delete(0, tkinter.END)
#         password_entry.delete(0, tkinter.END)
#
# window = tkinter.Tk()
# window.geometry('340x440')
# window.configure(bg='#333333')
#
# con = sqlite3.connect("mydatabase.db")
# txt = "CREATE TABLE IF NOT EXISTS signUp(username TEXT PRIMARY KEY, password TEXT NOT NULL)"
# con.execute(txt)
#
# frame = tkinter.Frame(bg='#333333')
#
# login_label = tkinter.Label(frame, text="Hello ! ", bg='#333333', fg='#fff', font=("Arial",30))
# first_name_label = tkinter.Label(frame, text="First Name", bg='#333333', fg="#fff", font=("Arial",16))
# first_name_input = tkinter.Entry(frame, font=("Arial",16))
# last_name_label = tkinter.Label(frame, text="Last Name", bg='#333333', fg="#fff", font=("Arial",16))
# last_name_input = tkinter.Entry(frame, font=("Arial",16))
# password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='#fff', font=("Arial",16))
# password_entry = tkinter.Entry(frame, show="*", font=("Arial",16))
# confirm_password_label = tkinter.Label(frame, text="Confirm Password", bg='#333333', fg='#fff', font=("Arial",16))
# confirm_password_entry = tkinter.Entry(frame, show="*", font=("Arial",16))
# login_button = tkinter.Button(frame, text="Login", bg="#ff3399", fg="#fff", font=("Arial",16), command=lambda: signin(username_input.get(), password_entry.get()))
# signup_button = tkinter.Button(frame, text="Sign Up", bg="#33cc33", fg="#fff", font=("Arial",16), command=sign_up)
#
# login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
# first_name_label.grid(row=1, column=0)
# first_name_input.grid(row=2, column=1, pady=20)
# last_name_label.grid(row=1, column=1)
# last_name_input.grid(row=2, column=2, pady=20)
# # password_label.grid(row=2, column=0)
# # password_entry.grid(row=2, column=1, pady=20)
# # login_button.grid(row=3, column=0, columnspan=2, pady=10)
# # signup_button.grid(row=4, column=0, columnspan=2, pady=10)
#
# frame.pack()
# window.mainloop()

import tkinter
import sqlite3
import re
import bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

window = tkinter.Tk()
window.geometry('340x440')
window.configure(bg='#333333')

con = sqlite3.connect("mydatabase.db")
# checking = "SELECT  FROM sqlite_master WHERE type='table' AND name='{table_name}';

# txt = "CREATE TABLE if not exists signUp(username TEXT PRIMARY KEY, password TEXT NOT NULL)"
# con.execute(txt)
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password
def signup():
    print(repr(username_input.get()))
    print(password_entry)
    print("Hello")
    # inst = "INSERT INTO signIn VALUES('"+ username +"','" + password +"')"
    # inst = f"INSERT INTO signUp VALUES('{username_input.get()}', '{password_entry.get()}')"
    # con.execute(inst)
    # slt = "SELECT * from signUp"
    # output = con.execute(slt)
    # print(output.fetchall()[0][0])
    # Connect to SQLite database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS signUp
                     (username TEXT, password TEXT)''')
    hashpass = generate_password_hash(password_entry.get())
    # Insert username and password into the table
    c.execute("INSERT INTO signUp (username, password) VALUES (?, ?)", (username_input.get(), hashpass))

    # Commit changes and close connection
    conn.commit()
    conn.close()

def signin(name, password):

    x=re.search("^[A-Za-z][A-Za-z0-9]{4,10}",name)
    p = re.search("[^\\s]{8,}", password)
    if x==None or p ==None:
        print("Invalid username or password")
    else:
        print(x)
        check =f"SELECT * from signUp where username='{name}' and password='{password}'"
        output = con.execute(check)
        result = output.fetchone()
        # print(result)
        if result == None:
            print("Username or password does not exist")
        else:
            print(f"Hello there ! {name}")
# signin("wande","hello")
frame = tkinter.Frame(bg='#333333')
#creating widgets
#it implies the end of the page, any line of code after the mainloop() method will not run
login_label = tkinter.Label(frame, text="Welcome back! ", bg='#333333', fg='#fff', font=("Arial",30))
username_label= tkinter.Label(
    frame,text ="Username",bg='#333333', fg="#fff",font=("Arial",16))
username_input = tkinter.Entry(frame,font=("Arial",16))
password_entry= tkinter.Entry(frame,show ="*",font=("Arial",16))
password_label= tkinter.Label(
    frame,text ="Password",bg='#333333',fg='#fff',font=("Arial",16))
# username_input.pack()

def p():
    print(username_input.get())
login_button = tkinter.Button(frame, text="Login", bg="#ff3399",fg="#fff",font=("Arial",16), command=signup)
#placing widgets
login_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_input.grid(row=1, column=1,pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)
frame.pack()
window.mainloop()
