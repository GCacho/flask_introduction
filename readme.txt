# Introducción a Flask

## Instalar y activar ambiente virtual 
    - python3 -m venv venv
    - source venv/bin/activate

## Instalar flask y librerias necesarias
    - pip install -r requirements.txt

## Definir la nueva variable en flask (terminal)
    - export FLASK_APP=main.py
    - echo $FLASK_APP

## Iniciar el debuger de flask
    - export FLASK_ENV=development
    - echo $FLASK_ENV

## Correr el servidor de Flask
    - flask run