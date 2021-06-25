from flask import Blueprint, request, jsonify
import models.user_model as User
import json
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token,set_access_cookies,unset_jwt_cookies

auth_router = Blueprint('auth', __name__,
                        url_prefix='/api/auth')

@auth_router.route('/register', methods=['POST'])
@cross_origin()
def register():
    user_to_create = request.json
    existing_user = User.find_by_username(user_to_create['username'])
    if existing_user:
        return "Username already taken", 500
    created_user = User.create(user_to_create['username'],user_to_create['password'])
    access_token = create_access_token(created_user['id'])
    response = jsonify()
    set_access_cookies(response,access_token)
    return response, 200


@auth_router.route('/login',methods=['POST'])
@cross_origin()
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.authenticate(username,password)
    if user:
        access_token = create_access_token(user['id'])
        response = jsonify()
        set_access_cookies(response,access_token)
        return response, 200
    return 'login failed',400
    

@auth_router.route('/logout',methods=['POST'])
@cross_origin()
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response,200

