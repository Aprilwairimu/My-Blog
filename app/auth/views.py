from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from . import auth
from flask_login import login_user,logout_user,login_required


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
   
    return render_template('auth/register.html', registration_form = form )


@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()


    title = "Blog login"
    return render_template('auth/login.html',title=title,login_form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
