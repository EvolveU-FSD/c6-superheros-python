from flask import Blueprint, request
from flask_cors import cross_origin
import json

from models.superhero_sqlite import Superhero

superhero = Blueprint('superhero',__name__,url_prefix='/api/superhero')

@superhero.route('/',methods=['GET'])
@cross_origin()
def superhero_route():
    data = Superhero.find_all()
    return json.dumps(data)

@superhero.route('/',methods=['POST'])
def create_superhero():
    superhero_to_create = request.json
    print(superhero_to_create)
    created_superhero = Superhero.create(superhero_to_create)
    return json.dumps(created_superhero)

@superhero.after_request # need for cors
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response