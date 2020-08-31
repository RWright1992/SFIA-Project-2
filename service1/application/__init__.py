#importing Flask form flask module
from flask import Flask
# create a new instance of Flask and store it in app 
app = Flask(__name__)
#importing routes.py
from application import routes
