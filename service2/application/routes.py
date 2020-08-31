#importing Response from flask module
from flask import Response
#importing app object from __init__.py
from application import app
#importing generate username function from random_username.generate module
from random_username.generate import generate_username

#creating route which will generate random username
@app.route('/user/randomname', methods = ['GET'])
def user_name1():
	username = generate_username()
	return Response(username, mimetype='text/plain')
