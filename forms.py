from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    page = StringField('Page', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    coverPhoto = StringField('Cover Photo', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')
