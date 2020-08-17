from flask import Flask
import os
from os import getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

from application import routes
