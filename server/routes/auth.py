from flask import Blueprint
auth_router = Blueprint('auth', __name__, url_prefix="/api/auth")
from werkzeug.security import generate_password_hash
from flask import request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, \
  unset_jwt_cookies, jwt_required
import models.user_model as User

@auth_router.route('/register', methods=('POST',))
def register():
  user = request.json
  
  found_user = User.find_by_username(user['username'])
  if found_user is None:
    created_user = User.create(user)
    access_token = create_access_token(created_user['id'])

    response = jsonify()
    set_access_cookies(response, access_token)

    return response, 201
  else:
    
    return jsonify(message="Unable to create user."), 400

@auth_router.route('/login', methods=('POST',))
def login():
  data = request.json
  username = data['username']
  password = data['password']
  user = User.authenticate(username, password)
  if user:
    access_token = create_access_token(identity=user['id'])

    response = jsonify()
    set_access_cookies(response, access_token)
    return response, 201
  else:
    return jsonify(message="Unauthorized"), 401


@auth_router.route('/logout', methods=['POST'])
@jwt_required()
def logout():
  response = jsonify()
  unset_jwt_cookies(response)
  return response, 200