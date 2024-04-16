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
def signup(name,password):
    # x = re.search("^[A-Za-z][A-Za-z0-9]{4,10}", name)
    # p = re.search("[^\\s]{8,}", password)
    # if x == None or p == None:
    #     print("Invalid username or password")
    #     return False
    # hashpass = hash_password(
    #     password)
    # Insert username and password into the table
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
def signin(name, password):
    # x = re.search("^[A-Za-z][A-Za-z0-9]{4,10}$", name)
    # p = re.search("[^\\s]{8,}", password)
    # if x is None or p is None:
    #     print("Invalid username or password")
    #     return False
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

        return True
