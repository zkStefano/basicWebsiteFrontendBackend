#---------  a cosa serve views.py ?--------------------------

#views.py serve a definire il routing del sito #

from flask import Blueprint, render_template

views = Blueprint('views', __name__)  #fai sempre così

@views.route('/')
def home():
    return render_template("home.html")


