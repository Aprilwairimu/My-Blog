from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,PasswordField
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
	title = StringField('Title')
	description = TextAreaField("What would you like to Blog about ?")
	submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Pitch review', validators=[InputRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')