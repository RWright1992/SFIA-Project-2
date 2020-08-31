#importing Response from flask module
from flask import Response
#importing app object from __init__.py
from application import app
#importing generate username function from random_username.generate module
from random_username.generate import generate_username
#importing randint function from random module
from random import randint

#creating route which will generate random username
'''
@app.route('/user/randomname', methods = ['GET'])
def user_name1():
	username = generate_username()
	return Response(username, mimetype='text/plain')
'''
#creating 2nd implementation for service 2 which will generate random number

@app.route('/user/randomname', methods = ['GET'])
def user_name1():
	usernumber = random.randint(0,9)
	text = 'winner'
	username =  text + usernumber
	return Response(username, mimetype='text/plain')

