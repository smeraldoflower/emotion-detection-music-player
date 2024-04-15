import sqlite3
import re
con = sqlite3.connect("mydatabase.db")
# checking = "SELECT  FROM sqlite_master WHERE type='table' AND name='{table_name}';

txt = "CREATE TABLE if not exists signUp(username TEXT PRIMARY KEY, password TEXT NOT NULL)"
con.execute(txt)
def signup(username, password):
    # inst = "INSERT INTO signIn VALUES('"+ username +"','" + password +"')"
    inst = f"INSERT INTO signUp VALUES('{username}', '{password}')"
    con.execute(inst)
    # slt = "SELECT * from signUp"
    # output = con.execute(slt)
    # print(output.fetchall()[0][0])

signup("wande", "hello")
def signin(name, password):

    x=re.search("^[A-Za-z][A-Za-z0-9]{4,10}",name)
    p = re.search("[^\\s]{8,}", password)
    if x==None or p ==None:
        print("Invalid username")
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
signin("wandeHassann","helloworld")

