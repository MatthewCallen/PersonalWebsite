#store standard routes for website(i.e. login page, home page, etc.)
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

