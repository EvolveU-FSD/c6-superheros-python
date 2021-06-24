from flask import Blueprint, request, after_this_request
import models.superhero_model as Superhero
import json
from flask_cors import cross_origin

superhero_router = Blueprint('superhero', __name__,
                        url_prefix='/api/superhero')

@superhero_router.route('/<int:id>')
@cross_origin()
def find_by_id(id):
    print(id)
    result = Superhero.find_by_id(id)
    if 'error' in result:
        return {"error":"invalid id"}
    else:
        return result
@superhero_router.route('/',methods=['GET'])
@cross_origin()
def find_all_superheros():
    
    result = Superhero.find_all()
    return json.dumps(result)
    

@superhero_router.route('/',methods=['POST'])
@cross_origin()
def create_superhero():
    superhero_to_add = request.json
    Superhero.create(superhero_to_add)
    return "success"

@superhero_router.route('/<int:id>',methods=['PUT'])
@cross_origin()
def update_superhero(id):
    superhero_to_update = request.json
    Superhero.update(id,superhero_to_update)
    return "success"




