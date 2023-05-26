import bcrypt
import json
import os
import requests

from math import floor
from sqlalchemy.sql import func
from sqlalchemy.types import String, Integer, DateTime, JSON, Text

from dataclasses import dataclass
from flask import (
    Flask,
    jsonify,
    url_for,
    render_template,
    send_from_directory,
    request,
    Response,
)
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape


app = Flask(__name__, static_url_path="", static_folder="client/build")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://abrahamesparza@localhost:5432/quiz_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)

salt = bcrypt.gensalt()


@dataclass
class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(String(100), nullable=False)
    last_name = db.Column(String(100), nullable=False)
    username = db.Column(String(100), nullable=False)
    email = db.Column(String(100), nullable=False, unique=True)
    password = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<User {self.username}>"


@dataclass
class Quizzers(db.Model):
    __tablename__ = "quizzer"

    id = db.Column(Integer, primary_key=True)
    correct_responses = db.Column(Integer, nullable=True)
    incorrect_responses = db.Column(Integer, nullable=True)
    total_questions = db.Column(Integer, nullable=True)
    questions = db.Column(JSON, nullable=False)
    quizzer_id = db.Column(Integer, db.ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"<Quizzer {self.quizzer_id}"


# --------------ROUTES-----------------
@app.get("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


# GET Users information from database
@app.get("/db/users")
def retrieve_users():
    users = Users.query.all()
    users_list = []
    for user in users:
        user_id = user.id
        user_name = user.username
        full_name = f"{user.first_name} {user.last_name}"
        password = user.password
        users_list.append(
            {
                "id": user_id,
                "username": user_name,
                "full_name": full_name,
                "password": password,
            }
        )
    return users_list


@app.get("/db/quizzer")
def retriever_quizzer():
    quizzer = Quizzers.query.all()
    quizzer_list = []
    for quiz in quizzer:
        quizzer_id = quiz.quizzer_id
        total_questions = quiz.total_questions
        correct_responses = quiz.correct_responses
        incorrect_responses = quiz.incorrect_responses
        # questions = quiz.questions - need to fix formatting of how json is stored
        quizzer_list.append(
            {
                "quizzer_id": quizzer_id,
                "total_questions": total_questions,
                "incorrect_responses": incorrect_responses,
                "correct_responses": correct_responses,
                "overall_scrore": floor((correct_responses / total_questions) * 100),
            }
        )
    return quizzer_list


# POST information to database
@app.post("/user/signup")
def signup_user():
    data = json.loads(request.data)
    password = data["password"].encode("utf-8")
    hashed_pw = bcrypt.hashpw(password, salt)
    new_user = Users(
        first_name=data["firstName"],
        last_name=data["lastName"],
        username=data["username"],
        email=data["email"],
        password=hashed_pw,
    )
    db.session.add(new_user)
    db.session.commit()

    return send_from_directory(app.static_folder, "index.html"), 201


class QuizMaker(Resource):
    """
    Instatiating my REST API using flask-restful
    allows me to create the get, post, delete, put, etc.

    a resource will need to be added to the class below it
    """

    def get(self):
        api_url = "https://opentdb.com/api.php?amount=5"
        response = requests.get(api_url)
        print(f"response: response")
        data = response.json()
        results = data["results"]
        print(f"data!: {results}")
        return results


api.add_resource(QuizMaker, "/quiz")


# class LoginUser(Resource):
#     def post(self):
#         data = request.data
#         return Response(data, status=201, mimetype='application/json')


# api.add_resource(LoginUser, '/create_new_user')
