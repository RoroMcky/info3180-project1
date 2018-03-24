from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired()])
    LastName = StringField('Last Name', validators=[DataRequired()])
    Gender=SelectField('Gender', choices=[("None", "Select Gender"),('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    Email=StringField('Email', validators=[DataRequired(), Email()])
    Location=StringField('Location',validators=[DataRequired()])
    Biography=TextAreaField('Biography',validators=[DataRequired()])
    picture = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'])])