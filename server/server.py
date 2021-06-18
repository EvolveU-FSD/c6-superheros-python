
from flask import Flask

from routes.superhero import superhero_router

app = Flask(__name__)
app.register_blueprint(superhero_router)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()