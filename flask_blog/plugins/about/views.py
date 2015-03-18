from flask import Blueprint
from flask import render_template

about = Blueprint('about', __name__, template_folder='templates')

@about.route("/about")
def index():
    return render_template('about.html')
