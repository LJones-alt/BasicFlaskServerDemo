
import csv
import json
import os
from flask import Flask, jsonify, render_template, request, send_file
import io
from flask_csv import send_csv
import os
from plantData import PlantData

app = Flask(__name__)

## Landing page
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/addPlant", methods=['POST'])
def addPlant(plantname):
  plantName = PlantData.addplant(plantname, plantobj)

## type in the route
@app.route('/sendRecieve', methods=['GET'])
def sendRecieve():


    return jsonify({"result" : "Sucsess"})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)