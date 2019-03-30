from flask import Flask, request, render_template
import os

app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/heatmap", methods=["GET"])
def heatmap():
    return render_template("heatmap.html")


if __name__ == "__main__":
    app.run(debug=True)
