from flask import Flask, redirect, request, make_response

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
    return "Hello World Flask!, tu IP es {}".format(user_ip)