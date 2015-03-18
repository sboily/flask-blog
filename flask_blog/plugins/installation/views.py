from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_blog.extensions import mongo
from forms import InstallBlogForm, InstallUserForm

installation = Blueprint('installation', __name__, template_folder='templates')

@installation.route("/install", methods=["GET", "POST"])
def index():
    is_installed = mongo.db.blog.find_one()
    if is_installed:
        return redirect(url_for("home.index"))

    form = InstallBlogForm()
    userform = InstallUserForm()
    if form.validate_on_submit():
        mongo.db.blog.insert(form.data)
        mongo.db.users.insert(userform.data)
        return redirect(url_for("home.index"))
    return render_template('index.html', form=form, userform=userform)
