#---------  a cosa serve views.py ?--------------------------

#views.py serve a definire il routing del sito #

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db



views = Blueprint('views', __name__)  #fai sempre così

@views.route('/', methods = ['GET','POST'])
@login_required  #posso accedere alla homepage se ho fatto la login.
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has been added', category='success')

    return render_template("home.html", user=current_user)


