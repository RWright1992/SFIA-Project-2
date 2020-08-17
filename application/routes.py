from flask import render_template, url_for, redirect, request
from application.forms import QuestionForm
from application import app

#define route for homepage to be displayed
@app.route('/')
@app.route('/magic8ball')
def home():
    return render_template('magic8ball.html', title='Home')