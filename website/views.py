from flask import Blueprint, render_template
from flask_login import current_user, login_required

# Setting up Blueprint for Flask application, name of this blueprint is views
views = Blueprint('views', __name__)

# Defining rout 
@views.route('/')
@login_required
# This f will run whenever we go to / route
def home():
  return render_template('home.html', user=current_user)


