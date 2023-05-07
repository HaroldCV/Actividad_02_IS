from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import bcrypt

app = Flask(__name__)
CORS(app)

secretPass = "abcd"
API_KEY_VAL = "12345"

@app.route('/external-api', methods=['POST'])
@cross_origin(origins=['http://localhost:3000'])
def happy():
    data = request.json
    if not data:
        return jsonify(error="request body cannot be empty"), 400
    api_key_val = data["api_key"]
    hashed_api_key = bcrypt.hashpw(api_key_val.encode('utf-8'), secretPass.encode('utf-8'))
    if not bcrypt.checkpw(API_KEY_VAL.encode('utf-8'), hashed_api_key):
        return jsonify(result="You are not welcome Here !!")
    response = jsonify(result="Im your father Luke !")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5002)
