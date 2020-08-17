from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

#creating a back end form to allow for question to be input
class QuestionForm(FlaskForm):
    question = StringField('What is your question?',
        validators= [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )