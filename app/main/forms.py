from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,PasswordField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')