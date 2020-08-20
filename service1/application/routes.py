#importin render_template redirect and url_for from flask module
from flask import render_template, redirect, url_for
#importing app object from __init__.py
from application import app
#importing requests
import requests

#route for homepage
@app.route('/', methods=['GET'])
def home():
	return render_template('home.html', title='Home')

#route for generating random username + game
@app.route('/username/game', methods = ['GET'])
	username = requests.get('http://service2:5001/user/randomname')
	game = requests.get('http://service3:5002/user/randomgame')
	return render_template('namegame.html', title='Username and Game', username=username.txt, game=game.txt)
