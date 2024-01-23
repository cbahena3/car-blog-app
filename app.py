import db
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/cars.json')
def index():
    return db.cars_all()

@app.route("/cars/<id>.json")
def show(id):
    return db.cars_find_by_id(id)