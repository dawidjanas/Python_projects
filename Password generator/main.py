import random
from sqlite3.dbapi2 import connect
import string
import sqlite3

while True:
    try:
        site = input("Enter site or application name that you want to generate password for: ")
        if site.lower() == 'done': quit()
        password_lenght = input("Enter password lenght: ")

        conn_connect = sqlite3.connect("passwords.sqlite")
        cur = conn_connect.cursor()

        letters = string.ascii_letters
        num = string.digits
        symbols = string.punctuation
        all = letters + num + symbols

        temp = random.sample(all, int(password_lenght))
        password = "".join(temp)

        cur.execute('INSERT INTO Passwords (Name, password) VALUES (?, ? )', (site, password))
        conn_connect.commit()
        cur.close()
    except:
        print("ERROR")
        quit()

