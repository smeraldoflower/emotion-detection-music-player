import tkinter
import sqlite3
import re
from werkzeug.security import generate_password_hash,check_password_hash

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS signUp
                     (username TEXT, password TEXT)''')

def hash_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password

def signup(name, password, label):
    # Insert username and password into the table
    c.execute(f"SELECT * FROM signUp where username='{name}'")
    # "checks where user already exists "
    if c.fetchone():
        label.config(text="Username already exist")
        print("User already exist")
        return
    try:
        c.execute("INSERT INTO signUp (username, password) VALUES (?, ?)", (name, password))
        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Sign up successful")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists")
        return False

def signin(name, password, label):
    """ Insert data into the database
    :return False if username or password is incorrect
    :return True if username and password successful authenticates
    """
    con = sqlite3.connect("mydatabase.db")
    check = f"SELECT * FROM signUp WHERE username='{name}'"
    output = con.execute(check)
    result = output.fetchone()
    con.close()

    if result is None or not check_password_hash(result[1], password):
        label.config(text="Username or Password is incorrect")
        print("Username or Password is incorrect")
        return False
    else:
        print(f"Hello there, {name}!")

        return True
