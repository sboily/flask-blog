from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import Required
import datetime

class PostsForm(Form):
    title = TextField('title', [Required()])
    preview = TextAreaField('preview', [Required()])
    body = TextAreaField('body', [Required()])
    tags = TextField('tags')
    date = DateTimeField(default=datetime.datetime.utcnow())
    submit = SubmitField('Submit')
    submit_preview = SubmitField('Preview')

