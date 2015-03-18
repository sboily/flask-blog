from flask import Blueprint
from flask import render_template
from flask.ext.login import login_required
from flask_blog.extensions import mongo
from flask_blog.helpers import convertToObj
from forms import SettingsForm
from bson import ObjectId

settings = Blueprint('settings', __name__, template_folder='templates')

@settings.route("/settings", methods=["GET", "POST"])
@login_required
def index():
    settings = mongo.db.blog.find_one()
    id = ObjectId(settings['_id'])
    form = SettingsForm(obj=convertToObj(**settings))
    if form.validate_on_submit():
        form.populate_obj(convertToObj(**settings))
        mongo.db.blog.update({'_id': id},
                             {'$set': form.data}
                            )
    return render_template('settings.html', form=form)
