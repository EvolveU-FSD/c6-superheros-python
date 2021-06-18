from flask import Flask
app = Flask(__name__, static_folder='../client/build')
from routes.superhero import superhero

@app.route('/static/<path:path>')
def react(path):
    print(path)
    return app.send_static_file('static/'+path)



@app.route('/')
def home():
    print('here')
    return app.send_static_file('index.html')


app.register_blueprint(superhero)
if __name__ == '__main__':
    app.run(port=5000)




