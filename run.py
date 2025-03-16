from flask import Flask, request, jsonify
from src import UserRepo

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "ola, estou na aplicação setada"

@app.route('/insert', methods=['POST'])
def insert():

    body = request.json
    userRepo = UserRepo()

    userRepo.insert_user(body['name'])

    return jsonify({
        "response": "OK"
    }), 201

app.run(debug=True)