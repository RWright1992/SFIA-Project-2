#importing Response from flask module
from flask import Response
#importing app object from __init__.py
from application import app
#importing randint function from random module
from random import randint

#creating route which will generate random switch online game
@app.route('/user/randomgame', methods = ['GET'])
def user_name1():
	games = ['Mario Kart','Monster Hunter Generations','Tetris 99' ]
	return Response(games[randint(0,2)], mimetype='text/plain')

