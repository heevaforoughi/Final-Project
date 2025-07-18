from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("HomePage.html")
@app.route("/Basketball")
def bball():
    return render_template("Basketball.html")
@app.route("/Tennis")
def tenis():
    return render_template("Tennis.html")
@app.route("/Soccer")
def soc():
    return render_template("Soccer.html")
@app.route("/opinion")
def op():
    return render_template("opinion.html")
