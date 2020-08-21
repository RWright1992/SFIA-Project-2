#importing Response and request from flask module
from flask import Response, request
#importing app object from __init__.py
from application import app
#importing randint function from random module
from random import randint
#importing generate username function from random_username.generate module
from random_username.generate import generate_username

#creating route which will generate random username
@app.route('/user/8ball', methods = ['GET','POST'])
def game_prediction():
	name_game = request.data.decode('utf-8')
	split_string = name_game.split(",")
	username_text = split_string[0]
	game_text = split_string[1]
	user_number = username_text[-1]
	if game_text == 'Mario Kart' and user_number == '9':
		prediciton = "You will finish 9th on Kart"
	elif game_text == 'Mario Kart' and user_number == '8':
		predicition = "You will finish 8th on Kart"
	elif game_text == 'Mario Kart' and user_number == '7':
		predicition = "You will finish 7th on Kart"
	elif game_text == 'Mario Kart' and user_number == '6':
		predicition = "You will finish 6th on Kart"
	elif game_text == 'Mario Kart' and user_number == '5':
		predicition = "You will finish 5th on Kart"
	elif game_text == 'Mario Kart' and user_number == '4':
		predicition = "You will finish 4th on Kart"
	elif game_text == 'Mario Kart' and user_number == '3':
		predicition = "You will finish 3rd on Kart"
	elif game_text == 'Mario Kart' and user_number == '2':
		predicition = "You will finish 2nd on Kart"
	elif game_text == 'Mario Kart' and user_number == '1':
		predicition = "Blue Shell"
	elif game_text == 'Mario Kart' and user_number == '0':
		predicition = "Just go outside today"
	elif game_text == 'Tetris 99' and user_number == '9':
		prediciton = "You will finish 9th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '8':
		predicition = "You will finish 8th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '7':
		predicition = "You will finish 7th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '6':
		predicition = "You will finish 6th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '5':
		predicition = "You will finish 5th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '4':
		predicition = "You will finish 4th on Tetris"
	elif game_text == 'Tetris 99' and user_number == '3':
		predicition = "You will finish 3rd on Tetris"
	elif game_text == 'Tetris 99' and user_number == '2':
		predicition = "You will finish 2nd on Tetris"
	elif game_text == 'Tetris 99' and user_number == '1':
		predicition = "Tetris Maximus"
	elif game_text == 'Tetris 99' and user_number == '0':
		predicition = "Maybe you should take up knitting"
	elif game_text == 'Monster Hunter Generations' and user_number == '9':
		prediciton = "Save the monsters"
	elif game_text == 'Monster Hunter Generations' and user_number == '8':
		predicition = "I wouldn't trust thoses villagers"
	elif game_text == 'Monster Hunter Generations' and user_number == '7':
		predicition = "Maybe hunt a few monsters"
	elif game_text == 'Monster Hunter Generations' and user_number == '6':
		predicition = "Better eat before you go hunting"
	elif game_text == 'Monster Hunter Generations' and user_number == '5':
		predicition = "Cats are cool"
	elif game_text == 'Monster Hunter Generations' and user_number == '4':
		predicition = "Gis yer materials"
	elif game_text == 'Monster Hunter Generations' and user_number == '3':
		predicition = "Need better hunting gear"
	elif game_text == 'Monster Hunter Generations' and user_number == '2':
		predicition = "Capture the boyo"
	elif game_text == 'Monster Hunter Generations' and user_number == '1':
		predicition = "Are you really sure you want to do this"
	elif game_text == 'Monster Hunter Generations' and user_number == '0':
		predicition = "Danger ahead"
	else:
		predicition = "Jive Turkey"
	return Response(predicition, mimetype= 'text/plain')
	

