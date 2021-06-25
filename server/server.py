
from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from routes.superhero import superhero_router
from routes.auth import auth_router
app = Flask(__name__)
app.register_blueprint(superhero_router)
app.register_blueprint(auth_router)
app.config["JWT_SECRET_KEY"]="hello"
app.config["JWT_TOKEN_LOCATION"]=['cookies'] 
app.config["JWT_COOKIE_SECURE"]=False # must be true in production
app.config["JWT_COOKIE_CSRF_PROTECT"]=False # must be true in production
JWTManager(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/secure')
@jwt_required()
def secure():
    return "you are authorized"
app.run()
