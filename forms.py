#from flask-wtf import Flask-WTF
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')
     