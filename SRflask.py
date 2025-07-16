from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Sport Player Rankings </h1>"