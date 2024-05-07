# Authors: Yewande Hassan, Kwame Addo
# File: db.py

# Relative File path code referenced and incorporated from : https://isaacstechblog.com/blog/sqlite3-in-python/

import tkinter
import os
import sqlite3
import re
from werkzeug.security import generate_password_hash,check_password_hash

# ----- Builds relative file path for database file in Database directory ----- #

# the relative file path
path = 'mydatabase.db'

# get the path to the directory this script is in
scriptdir = os.path.dirname(__file__)
# add the relative path to the database file from there
db_path = os.path.join(scriptdir, path)
# make sure the path exists and if not create it
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# ------------------------------------------------------------------------------ #

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS signUp
                     (username TEXT, password TEXT)''')

def hash_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password

def signup(name, password, label):
    # Insert username and password into the table
    # conn = sqlite3.connect('mydatabase.db')
    con = sqlite3.connect(db_path)   
    c = con.cursor()
    c.execute(f"SELECT * FROM signUp where username='{name}'")
    # "checks where user already exists "
    if c.fetchone():
        label.config(text="Username already exists")
        print("User already exists")
        return
    try:
        c.execute("INSERT INTO signUp (username, password) VALUES (?, ?)", (name, password))
        # Commit changes and close connection
        con.commit()
        con.close()
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
    con = sqlite3.connect(db_path)
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
