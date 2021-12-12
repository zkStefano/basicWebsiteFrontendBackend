from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required,logout_user, current_user

auth = Blueprint('auth', __name__)  #fai sempre così


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # metto post perchè voglio che faccia il controllo solo se premo il bottone di login
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        # come fare le query:
        user = User.query.filter_by(email=email).first()  #faccio un primo controllo sulle email e salvo il risultato della query
        if user:
            if check_password_hash(user.password, password) :
                flash('Logged in successfully!', category='success')
                #il login effettivo si fa qui usando flask_login
                login_user(user, remember=True)
                redirect(url_for('views.home'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email doesn\'t exist', category='error')
    return render_template("login.html", user=current_user)




@auth.route('/logout')
@login_required #non posso fare logout se non ho fatto la login
def logout():
    logout_user() #log out current user
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    #definisco come raccolgo i dati da mandare al database
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #controllo se posso registrare l'utente
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #creo un nuovo utente nel database raccogliendo i dati inseriti nel form
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(user)
            return redirect(url_for('views.home',user=current_user))

    return render_template("sign_up.html")