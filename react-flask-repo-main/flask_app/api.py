from flask import Flask
from flask import request, jsonify
import logging
from flask_cors import CORS

# Here is a missing import ? Are we missing some hashing library ???

app = Flask(__name__)
CORS(app)
secretPass = "abcd"
API_KEY_VAL = "12345"

@app.route('/external-api', methods=['POST'])
def happy():
    data = request.json
    if not data:
        return jsonify(error="request body cannot be empty"), 400
    #print(data)
    api_key_val = data["api_key"]
    if api_key_val != API_KEY_VAL:
        return jsonify(result="You are not welcome Here !!")
    return jsonify(result="Im your father Luke !")

if __name__ == "__main__":
    #logging.getLogger('flask_cors').level = logging.DEBUG
    #app.logger.setLevel(logging.DEBUG)
    logging.info("app run")
    app.run(debug=True, port=5002)
