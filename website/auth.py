from flask import Blueprint, render_template, request
from flask_login import current_user

# Setting up Blueprint for Flask application
auth = Blueprint('auth', __name__)

# Defining routes
@auth.route('/login', methods = ['GET', 'POST'])
def login():
  return render_template('login.html', user=current_user)

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
  return render_template('signup.html', user=current_user)