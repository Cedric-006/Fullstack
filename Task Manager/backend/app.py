from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from models import db, User, Task
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
db.init_app(app)
jwt = JWTManager(app)

# Enable CORS-Cross Origin Resource Sharing) for all routes,allowing requets from https://localhost:5173
CORS(app, resources={r"/*": {"origin":"https://localhost5173"}})

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return"Task Manager backend is running"

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.querry.filter_by(username=data["username"]).first():
        return jsonify({"msg":"Username already exists, choose another name!"}), 400
    user = User(username =data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "Account created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.querry.filter_by(username=data["username"]).first()
    if not user or user.password !=data["password"]:
        return jsonify({"msg": "Invalid Credentials,either the username or password is wrong!" }), 401
    token = create_access_token(identity=str(user.id))
    return jsonify({"token": token})

@app.route("/tasks",methods=["POST"])
@jwt_required()
def add_task():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    start_time = datetime.now() if data["start_now"] else datetime.strptime(data['start_time'], "%Y-%m-%dT%H:%M")
    task = Task(
        title=data["title"],
            description= data.get("description"),
            start_time=start_time,
            duration=data["duration"],
            done=data.get("done", False),
            user_id=user_id
            )
    db.session.add(task)
    db.session.commit()
    return jsonify({"msg": "Task added"}), 201

@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())
    tasks = Task.querry.filter_by(user_id=user_id).all()
    return jsonify([
        {"id": t.id,
          "title": t.title,
            "description": t.description,
            "start_time": t.start_time.isoformat(),
              "duration": t.duration,
              "done": t.done
              } for t in tasks
              ])

if __name__ == "__main__":
    app.run(debug=True,port=5000)