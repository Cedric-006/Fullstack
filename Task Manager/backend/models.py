from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tasks = db.relationship("Task",backref="user", lazy=True)

class Task(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    description = db.Column(db.text, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False) #track task completion
    user_id = db.Column(db.Integer, db.Foreignkey("user.id,"), nullable=False)    