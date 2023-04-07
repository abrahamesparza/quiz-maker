import os
import requests
from sqlalchemy.sql import func

from dataclasses import dataclass
from flask import Flask, jsonify, url_for, render_template, send_from_directory, request, Response
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape


app = Flask(__name__, static_url_path='', static_folder='client/build')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://abrahamesparza@localhost:5432/quiz_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

@dataclass
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    def __repr__(self) -> str:
        return f'<User {self.username}>'


# GET Users information from db
@app.get('/db/users')
def retrieve_users():
    users = Users.query.all()
    users_list = []
    for user in users:
        user_id = user.id
        user_name = user.username
        users_list.append({'id': user_id, 'username': user_name})
    return users_list

# GET paths
@app.get('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.get('/landing')
def showcase_landing():
    return render_template('landing.html')

@app.get('/projects')
def showcase_projects():
    return '<p>list projects here</p>'

@app.get('/project/<path:name>')
def showcase_project_by_name(name):
    return f'Project: {escape(name)}'


class QuizMaker(Resource):
    """
    Instatiating my REST API using flask-restful
    allows me to create the get, post, delete, put, etc.

    a resource will need to be added to the class below it
    """
    def get(self):
        api_url = 'https://opentdb.com/api.php?amount=5'
        response = requests.get(api_url)
        print(f'response: response')
        data = response.json()
        results = data['results']
        print(f'data!: {results}')
        return results
    

class LoginUser(Resource):
    def post(self):
        data = request.data
        return Response(data, status=201, mimetype='application/json')
    

api.add_resource(QuizMaker, '/quiz')
api.add_resource(LoginUser, '/create_new_user')
