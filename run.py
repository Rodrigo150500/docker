from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "ola, estou na aplicação setada"

app.run(debug=True)