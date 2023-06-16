from flask import Flask
app = Flask(__name__)
import dbhelpers
import json

@app.get('/animals')
def get_all_animals():
    results = dbhelpers.run_procedure('call get_animal()', [])
    animal_json = json.dumps(results, default=str)
    return animal_json

@app.get('/dog')
def get_dogs():
    results = dbhelpers.run_procedure('call get_dog()', [])
    animal_json = json.dumps(results, default=str)
    return animal_json

@app.get('/cat')
def get_cat():
    results = dbhelpers.run_procedure('call get_cat()', [])
    animal_json = json.dumps(results, default=str)
    return animal_json

app.run(debug=True)