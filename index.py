from ast import literal_eval
import json
import requests

from flask import Flask, jsonify, url_for, render_template, send_from_directory, request, Response
from flask_restful import Api, Resource
from markupsafe import escape


app = Flask(__name__, static_url_path='', static_folder='client/build')
api = Api(app)


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

# @app.get('/quiz')
# def showcase_quiz():
#     quiz_url = 'https://opentdb.com/api.php?amount=5'
#     response = requests.get(quiz_url)
#     quiz_data = response.json()
#     return quiz_data

# """
# The below is an attempt to understand the use of
# url_for.

# Still need to learn some more about this.
# """

# with app.test_request_context():
#     print(url_for('showcase_landing'))

# Playing with request
# @app.post('/login')
# def login_user():
#     print(request.method)
#     print(request.data)
#     return request.data

