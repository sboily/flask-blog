from flask import Blueprint, render_template, redirect, url_for
from flask_blog.extensions import mongo
from flask_blog.helpers import convertToObj
from flask.ext.login import login_required, current_user
from forms import PostsForm

posts = Blueprint('posts', __name__, template_folder='templates',
                  static_folder='static', static_url_path='/%s' % __name__)


@posts.route("/posts")
@login_required
def list():
    posts = mongo.db.posts.find()
    return render_template('posts_list.html', posts=posts)

@posts.route("/posts/add", methods=['GET', 'POST'])
@login_required
def add():
    form = PostsForm()
    if form.validate_on_submit():
        mongo.db.posts.insert(_add_username(form.data))
        return redirect(url_for("posts.list"))
    return render_template('post_add.html', form=form)

@posts.route("/posts/get/<ObjectId:id>")
def get(id):
    post = mongo.db.posts.find_one_or_404(id)
    return render_template('post_get.html', post=post)

@posts.route("/posts/edit/<ObjectId:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post = mongo.db.posts.find_one_or_404(id)
    form = PostsForm(obj=convertToObj(**post))
    if form.validate_on_submit():
        form.populate_obj(convertToObj(**post))
        mongo.db.posts.update({'_id': id},
                              {'$set': form.data}
                             )
        return redirect(url_for("posts.list"))
    return render_template('post_edit.html', form=form, post=post)

@posts.route("/posts/delete/<ObjectId:id>")
@login_required
def delete(id):
    mongo.db.posts.remove(id)
    return redirect(url_for("posts.list"))

def _add_username(form):
    post = form
    post.update({"author": current_user.username})
    return post
