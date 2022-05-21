from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import Blog, User,Comment
from flask.views import View,MethodView
from .forms import BlogForm, CommentForm ,UpdateProfile
from .. import db
import requests,json



@main.route('/', methods = ['GET','POST'])
def index():
    form=CommentForm()
    quotes=requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    data=json.loads(quotes.content)
    
    title = 'Home'
   
    return render_template('home.html', title = title,data=data)
    



@main.route('/write', methods = ['GET','POST'])
@login_required
def write():
    form=BlogForm()
    
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.filter_by().first()
    title = 'Home'
    

    return render_template("writer.html",blog=blog,form=form)


@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data        
        new_comment = Comment(description = description)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('main.comment', ))    
        all_comments = Comment.query.filter_by(blog_id = blog_id).all()
   

@main.route('/blogs/new',methods = ['GET','POST'])
def blogs():
    user=current_user
    blogs=Blog.query.all()
    form=CommentForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()        
        return redirect(url_for('main.index'))


    return render_template("blogs.html",form=form ,comment_form=form,blogs=blogs)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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
