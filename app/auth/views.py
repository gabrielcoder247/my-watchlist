from flask import render_template,redirect,url_for
from .import auth 
from .forms import RegistrationForm,LoginForm
from ..models import User
from .. import db
from flask_login import flask_user


@auth.route('/login')
def login():

    return render_template('auth/login.html')

@auth.route('/register', methods =["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html',registration_form =form) 

@auth.route('/login', methods =['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user,verify_password