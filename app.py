from flask import Flask, request, render_template
import os, threading
import assistant

app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/heatmap", methods=["GET"])
def heatmap():
    return render_template("heatmap.html")

@app.route("/assistant", methods=["GET"])
def startcall():
    threading.Thread(target=assistant.run, args=()).start()
    return render_template("calling.html")



if __name__ == "__main__":
    app.run(debug=True)
