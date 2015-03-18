from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, IntegerField
from wtforms.validators import Required

class SettingsForm(Form):
    title = TextField('Blog title', [Required()])
    description = TextField('Blog description', [Required()])
    bypage = IntegerField('Number posts by page', [Required()])
    facebook = TextField('Facebook user')
    twitter = TextField('Twitter user')
    github = TextField('Github user')
    submit = SubmitField('Submit', default=15)
