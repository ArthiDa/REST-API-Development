from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'This is index page'

from controller import *