from flask import Blueprint

# Setting up Blueprint for Flask application, name of this blueprint is views
views = Blueprint('views', __name__)

# Defining rout 
@views.route('/')
# This f will run whenever we go to / route
def home():
  return '<h1>Test</h1>'


