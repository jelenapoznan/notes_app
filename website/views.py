from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user, login_required
from .models import Note
from . import db
import json

# Setting up Blueprint for Flask application, name of this blueprint is views
views = Blueprint('views', __name__)

# Defining rout 
@views.route('/', methods = ['GET', 'POST'])
@login_required
# This f will run whenever we go to / route
def home():
  if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
      flash('Note is too short!', category = 'error')
    else:
      new_note = Note(data = note, user_id = current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('Note added!', category = 'sucecss')
  return render_template('home.html', user=current_user)

@views.route('/delete-note', methods = ['POST'])
def delate_note():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
  return jsonify({})



