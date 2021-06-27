from flask import Flask, request, abort
import ast
from typing import Dict

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Test App Launched</h1>"

@app.route("/dummy/train",methods=["POST"])
def train():
    content = _parse_flask_request(request)
    result = {"Outcome":"Success"}
    if content["password"]  != "kusef1nderm1ndr":
        result =  {"Outcome":"Fail","Error":"training failed"}

    return result  

@app.route("/dummy/predict",methods=["POST"])
def predict():
    content = _parse_flask_request(request)
    result = {"Outcome":"Success"}
    if content["password"]  != "kusef1nderm1ndr":
        result =  {"Outcome":"Fail","Error":"prediction failed"}

    return result  

@app.route("/dummy/purge",methods=["DELETE"])
def purge():
    content = _parse_flask_request(request)
    result = {"Outcome":f"content received: {content} type: {type(content)}"}
    if content["password"]  != "kusef1nderm1ndr":
        result =  {"Outcome":"Fail","Error":"prediction failed"}

    return result  

@app.route("/dummy/logs",methods=["POST"])
def logs():
    content = _parse_flask_request(request)
    result = {"Outcome":"Success", "Nothing to report": True}
    if content["password"]  != "kusef1nderm1ndr":
        result =  {"Outcome":"Fail","Error":"app make oopsie"}

    return result

def _parse_flask_request(req: request) -> Dict:
    content = ast.literal_eval(req.get_data().decode("UTF-8"))
    return content

if __name__ == "__main__":
    app.run(debug=True)