from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    confirm_email = StringField('Confirm Email', validators=[DataRequired(), EqualTo('email')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=120)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=120)])
    message = StringField("Message", validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Sign Up For Newsletter')