#Flask
from flask import Flask
from flask import request
from flask import redirect, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr # Para capturar la ip del usuario.
    response = make_response(redirect('/hello')) # Nos redirige a /hello
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello') # Donde queremos que corra la app
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)