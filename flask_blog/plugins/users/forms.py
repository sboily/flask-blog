from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, PasswordField
from wtforms.validators import Required, EqualTo

class UserForm(Form):
    username = TextField('Username', [Required()])
    email = TextField('Email', [Required()])
    password = PasswordField('Password', [Required(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')
    submit = SubmitField('Submit')

class LoginForm(Form):
    username = TextField('username', [Required()])
    password = PasswordField('password', [Required()])
    submit = SubmitField('Login')
