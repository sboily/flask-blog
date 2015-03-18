from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, IntegerField, PasswordField
from wtforms.validators import Required, EqualTo

class InstallBlogForm(Form):
    title = TextField('Blog title', [Required()])
    description = TextField('Blog description', [Required()])
    bypage = IntegerField('Number by page', [Required()])

class InstallUserForm(Form):
    username = TextField('Username', [Required()])
    email = TextField('Email', [Required()])
    password = PasswordField('Password', [Required(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')
    submit = SubmitField('Submit')

