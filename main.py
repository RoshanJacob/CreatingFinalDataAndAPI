from flask import Flask, jsonify, request
from exoplanet_data import data

app = Flask(__name__)


@app.route('/')
def getAllData():
    return jsonify({
        "data": data,
        "message": "success!"
    }), 200


@app.route('/exoplanet')
def getExoplanetName():
    name = request.args.get("planet_name")
    planet_data = [
        each_item for each_item in data if each_item["name"] == name]

    return jsonify({
        "Planet Data": planet_data,
        "message": 'Success!'
    }), 200


app.run()
