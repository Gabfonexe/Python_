from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config') # Confirmando o modo de debug 


api = Api(app)