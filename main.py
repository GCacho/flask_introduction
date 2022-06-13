from flask import Flask

app = Flask(__name__)

@app.route('/') #Donde queremos que corra la app
def hello():
    return "Hello World Flask!"