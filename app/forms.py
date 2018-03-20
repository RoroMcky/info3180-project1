from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField,TextField
from wtforms.validators import DataRequired, Email, InputRequired 
from wtforms.widgets import TextArea
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class ProfileForm(FlaskForm):
    FirstName = TextField('First Name', validators=[InputRequired()])
    LastName = TextField('Last Name', validators=[InputRequired()])
    Gender=SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    Email=TextField('Email', validators=[DataRequired(), 'Email'])
    Location=TextField('Location',validators=[DataRequired()])
    Biography=TextField('Biography',validators=[DataRequired()],widget=TextArea())
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])