from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_blog.extensions import mongo

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
def index():
    is_installed = mongo.db.blog.find_one()
    if not is_installed:
        return redirect(url_for('installation.index'))

    posts = mongo.db.posts.find()
    return render_template('home.html', posts=posts)
