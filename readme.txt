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
    - flask run -> Si no funciona seguir los pasos hasta el final y volver a intentar

### Notas ###

- Macro: 
    -Son un conjunto de comandos que se invocan con una palabra clave,
    opcionalmente seguidas de parámetros que se utilizan como código 
    literal. Los Macros son manejados por el compilador y no por el 
    ejecutable compilado.
    -Los macros facilitan la actualización y mantenimiento de las 
    aplicaciones debido a que su re-utilización minimiza la cantidad 
    de código escrito necesario para escribir un programa.

- Tests
    - flask test

- google cloud
    - Instalar en wsl desde la pagina oficial de google.
        - Para Windows dirígete a https://cloud.google.com/sdk/docs/quickstart-windows
        - Para MacOS dirígete a link https://cloud.google.com/sdk/docs/quickstart-macos
        - Para Linux dirígete a https://cloud.google.com/sdk/docs/quickstart-linux
        - gcloud init --no-browser -> para correr gcloud desde wsl
        - gcloud auth application-default login --no-launch-browser -> para conectar la aplicacion