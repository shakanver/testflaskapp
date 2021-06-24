from flask import Flask, request
import ast
app = Flask(__name__)

@app.route("/dummy/train")
def train():
    pass

@app.route("/dummy/predict")
def predict():
    pass

@app.route("/dummy/purge")
def purge():
    pass

@app.route("/dummy/logs")
def logs():
    content = _parse_flask_request(request)
    if request["password"]  != "kusef1nderm1ndr":
        {"Outcome":"Fail"}

    return {"Outcome":"Success"}

def _parse_flask_request(req: request) -> Dict:
    content = ast.literal_eval(req.get_data().decode("UTF-8"))
    return content

if __name__ == "__main__":
    app.run(debug=True)