from flask import Flask, request, render_template
import os
import assistant

app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/heatmap", methods=["GET"])
def heatmap():
    return render_template("heatmap.html")

@app.route("/assistant", methods=["POST"])
def startcall():
    assistant.run()
    return "done"



if __name__ == "__main__":
    app.run(debug=True)
