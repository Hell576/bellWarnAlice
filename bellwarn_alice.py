#start: export FLASK_APP=app.py && python3 -m flask run --host=0.0.0.0 --cert=adhoc

from flask import Flask, request
import logging
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["POST"])
def main():
    logging.info(request.json)

    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "Gotovo"
    elif request.methods == "POST":
            response["response"]["text"] = "Оу! К нам гости, угадай в какой форме?"

    return json.dumps(response)