from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask.views import View,MethodView

@main.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')

