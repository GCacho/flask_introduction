#Flask
from ensurepip import bootstrap
from multiprocessing import context
from flask import Flask
from flask import request
from flask import redirect, make_response, render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


todos = ['Comprar Café', 'Enviar Solicitud de Compra', 'Entregar video a productor']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr # Para capturar la ip del usuario.
    response = make_response(redirect('/hello')) # Nos redirige a /hello
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello') # Donde queremos que corra la app
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template('hello.html', **context) # **context es igual a context=context / amplia el diccionario