from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,PasswordField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()