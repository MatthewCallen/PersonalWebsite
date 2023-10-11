from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/projects')
def projects():
    return "<p> Projects </p>"
@auth.route('/edcuation')
def education():
    return "<p> Education </p>"

@auth.route('/about-me')
def about_me():
    return "<p>about me</p>"