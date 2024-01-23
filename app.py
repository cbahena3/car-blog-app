import db
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/cars.json", methods=["POST"])
def create():
    title = request.form.get("name")
    description = request.form.get("description")
    image = request.form.get("image")
    make = request.form.get("make")
    model = request.form.get("model")
    color = request.form.get("color")
    year = request.form.get("year")
    return db.cars_create(title, description, image, make, model, color, year)

@app.route('/cars.json')
def index():
    return db.cars_all()
