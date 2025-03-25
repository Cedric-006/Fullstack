import sqlite3

from flask import Flask, session,redirect,render_template,request

app = Flask(__name__)
#Sessions : help the server keep track of who is using 
#That is a stateful sever - it helps keep track of users and their sessions
app.secret_key = "secretkey"

def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    
    connection.commit()
    connection.close()

init_db()

app.route("/todo")
def home():
    if("user_id") in session:
        return render_template("login.html")
def todo():
    #Ensure that the user is logged in first
    return "You have reached the todo"
def debug():

    app.run(debug-True)