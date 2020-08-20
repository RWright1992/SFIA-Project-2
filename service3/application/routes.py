#importing Response and request from flask module
from flask import Response, request
#importing app object from __init__.py
from application import app
#importing randint function from random module
from random import randint
#importing generate username function from random_username.generate module
from random_username.generate import generate_username

#creating route which will generate random switch online game
@app.route('/user/randomgame', methods = ['GET'])
def user_name1():
	games = ['Mario Kart','Monster Hunter Generations','Tetris 99','Mario Party', 'Splatoon 2', 'Super Smash Bros', 'Arms', 'Doom', 'Rocket League', 'Dragonball Fighter Z' ]
	return Response(games[randint(0,9)], mimetype='text/plain')

