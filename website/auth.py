from flask import Blueprint

# Setting up Blueprint for Flask application
auth = Blueprint('auth', __name__)

# Defining routes
@auth.route('/login')
def login():
  return "<p>Login</p>"

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
  return "<p>SignUp</p>"