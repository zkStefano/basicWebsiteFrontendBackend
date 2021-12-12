#---------  a cosa serve views.py ?--------------------------

#views.py serve a definire il routing del sito #

from flask import Blueprint, render_template
from flask_login import login_required,current_user

views = Blueprint('views', __name__)  #fai sempre così

@views.route('/')
@login_required  #posso accedere alla homepage se ho fatto la login.
def home():
    return render_template("home.html", user=current_user)


