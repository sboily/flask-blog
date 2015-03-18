from flask import Blueprint
from flask import render_template

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route("/contact")
def index():
    return render_template('contact.html')
