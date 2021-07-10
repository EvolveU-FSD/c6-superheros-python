
from flask import Flask
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
from routes.superhero import superhero_router
import models.user_model as User
from routes.auth import auth_router
app = Flask(__name__,static_folder='../client/build')
app.config['JWT_SECRET_KEY'] = 'kittens'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
JWTManager(app)
app.register_blueprint(superhero_router)
app.register_blueprint(auth_router)

@app.route('/static/<path:path>')
def react_static(path):
    return app.send_static_file('static/'+path)

@app.route("/")
def react_home():
    return app.send_static_file('index.html')
    
@app.route('/protected')
@jwt_required()
def protected():
    logged_in_user_id = get_jwt_identity()
    logged_in_user=User.find_by_id(logged_in_user_id)

    

    return logged_in_user
if __name__ == '__main__':
    app.run()