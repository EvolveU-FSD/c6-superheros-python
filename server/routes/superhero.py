from flask import Blueprint, request
from flask_cors import cross_origin
import json


import models.superhero_sqlite as Superhero

superhero = Blueprint('superhero',__name__,url_prefix='/api/superhero')
@superhero.route('/',methods=['GET'])
@cross_origin()
def superhero_route():
    data = Superhero.find_all()
    return json.dumps(data)

@superhero.route('',methods=['POST'])
def create_superhero():
    superhero_to_create = request.json
    print(superhero_to_create)
    created_superhero = Superhero.create(superhero_to_create)
    return json.dumps(created_superhero)

@superhero.route('/<int:id>')
def get_superhero_by_id(id):
    superhero = Superhero.find_by_id(id)
    return json.dumps(superhero)

