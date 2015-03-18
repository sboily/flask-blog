from flask import Blueprint
from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, logout_user, login_user
from flask_blog.helpers import convertToObj
from flask_blog.extensions import mongo, login_manager
from forms import UserForm, LoginForm
from models import UserLogin
from bson import ObjectId

users = Blueprint('users', __name__, template_folder='templates')

@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({"username": form.username.data})
        if user:
            user = UserLogin(**user)
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('home.index'))
    return render_template('login.html', form=form)

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route("/users")
@login_required
def list():
    users = mongo.db.users.find()
    return render_template('users_list.html', users=users)

@users.route("/users/add", methods=["GET", "POST"])
@login_required
def add():
    form = UserForm()
    if form.validate_on_submit():
        mongo.db.users.insert(form.data)
        return redirect(url_for("users.list"))
    return render_template('user_add.html', form=form, users=users)

@users.route("/users/edit/<ObjectId:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    user = mongo.db.users.find_one_or_404(id)
    form = UserForm(obj=convertToObj(**user))
    if form.validate_on_submit():
        form.populate_obj(convertToObj(**user))
        mongo.db.users.update({'_id': id},
                              {'$set': form.data}
                             )
        return redirect(url_for("users.list"))
    return render_template('user_edit.html', form=form, user=user)

@users.route("/users/get/<ObjectId:id>")
@login_required
def get(id):
    user = mongo.db.users.find_one_or_404(id)
    return render_template('users_get.html', user=user)

@users.route("/users/<ObjectId:id>")
@login_required
def delete(id):
    users = mongo.db.users.remove(id)
    return redirect(url_for("users.list"))

@login_manager.user_loader
def load_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        return UserLogin(**user)
    return None
