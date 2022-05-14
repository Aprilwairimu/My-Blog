from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask.views import View,MethodView
from .forms import UpdateProfile

@main.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')












@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
