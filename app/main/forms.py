from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
#from flask_pagedown.fields import PageDownField
from ..models import User


class NameFormLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(0, 64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(5, 25, 'Password is too Short')])
    submit = SubmitField('Submit')
    

class NameFormSignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(0, 64)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5, 25, 'Password is too Short')])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(10),
                                Regexp('^[0-9]', 0,
               'Phone Number must have only numbers')])
    submit = SubmitField('Submit')


class NameFormApps(FlaskForm):
    country = SelectField(u'Countries', choices=[('Global', 'World Wide'), ('India', 'India'), ('United Kingdom', 'United Kingdom'), ('United States of America', 'United States of America'), ('Pakistan', 'Pakistan')])
    submit = SubmitField('Submit')
    
class NameFormDice(FlaskForm):
    submit = SubmitField('Roll the Dice!')
    
class NameFormTambola(FlaskForm):
    submit = SubmitField('Trigger a Number')