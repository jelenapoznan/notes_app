from flask import Blueprint, render_template, request, flash
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
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
    elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
    elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
    elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
    else:
         flash('Account created!', category='success')

  return render_template('signup.html', user=current_user)