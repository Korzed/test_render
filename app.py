from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola 4°D del Andrés Bello!'