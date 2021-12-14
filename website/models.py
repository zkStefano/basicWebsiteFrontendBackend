from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #data --> corpo della nota
    data = db.Column(db.String(10000))
    #date(data temporale viene automaticamente settata con una funzione che prende la data attuale
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #la foreign key su user_id collega la tabella Note a User.


class User(db.Model, UserMixin):
    #definisco la classe user con i suoi attributi
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    #siccome un utente puo avere più note (1 a n) --> metto la seguente linea per indicare quale sono le mie note
    notes = db.relationship('Note')
