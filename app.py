from flask import Flask, request, render_template, redirect, url_for
import os, threading, json, websockets
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

@app.route("/assistant", methods=["POST"])
def startcall():
    # threading.Thread(target=assistant.run, args=()).start()
    data = request.get_json(force=True)
    threading.Thread(target=assistant.run_demo, args=data)
    return ""

@app.route("/calling", methods=["GET"])
def calling():
    return render_template("calling.html")

@app.route("/demo", methods=["GET"])
def demo_map():
    return render_template("demo.html") 

@app.route("/subscribe-ws", methods=["GET"])
def subscribe_ws():
    return

if __name__ == "__main__":
    app.run(debug=True)