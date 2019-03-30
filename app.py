from flask import Flask, request, render_template
import os, threading, json
import assistant, all_scores

app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/scoreRoute", methods=["POST"])
def score_route():
    data = str(request.get_json(force=True)).replace("'", "\"")
    dangers = all_scores.get_all_scores(data, "pickle_test.p", 0.00015)
    return json.dumps(dangers)

@app.route("/assistant", methods=["GET"])
def startcall():
    threading.Thread(target=assistant.run, args=()).start()
    return render_template("calling.html")

if __name__ == "__main__":
    app.run(debug=True)
