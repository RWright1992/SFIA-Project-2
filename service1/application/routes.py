#importin render_template redirect and url_for from flask module
from flask import render_template, redirect, url_for, request, jsonify
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
def namegame():
	username = requests.get('http://service2:5001/user/randomname')
	game = requests.get('http://service3:5002/user/randomgame')
	return render_template('namegame.html', title='Username and Game', username=username.text, game=game.text)

'''
@app.route('/username/prediction', methods = ['GET'])
def prediction():
	prediction = requests.get('http://service4:5003/user/8ball')
'''

#route for generating random username + game
@app.route('/username/game1', methods = ['GET', 'POST'])
def prediction():
	username = requests.get('http://service2:5001/user/randomname')
	game = requests.get('http://service3:5002/user/randomgame')
	username_text = username.text
	game_text = game.text
	middle = ','
	username_game = username_text + middle + game_text
	gamename_post = requests.post('http://service4:5003/user/8ball', data=username_game)
	return render_template('prediction.html', title="Should you play", prediction=gamename_post.text, username=username.text, game=game.text)
