from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')


@app.route('/sign_in', methods=['POST'])
@cross_origin()
def sign_in():
    data = request.json

    username = data.get('username')
    password = data.get('password')
    data = username + ',' + password

    with open('../login-microservice/loginRequest.txt', 'w') as file:
        file.write(data)

    # wait for microservice to write to text file before checking for response
    time.sleep(1)
    with open('../login-microservice/loginResponse.txt', 'r') as file:
        login = file.read()

    if login == 'True':
        response = {'authenticated': True}
    else:
        response = {'authenticated': False}

    return jsonify(response)


@app.route('/create', methods=['POST'])
@cross_origin()
def create():
    data = request.json

    username = data.get('username')
    password = data.get('password')
    data = username + ',' + password + '\n'

    with open('../login-microservice/createRequest.txt', 'w') as file:
        file.write(data)

    response = {'created': True}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
