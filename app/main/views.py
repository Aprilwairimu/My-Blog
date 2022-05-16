from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import Blog, User,Comment
from flask.views import View,MethodView
from .forms import UpdateProfile
from .forms import BlogForm, CommentForm

@main.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')


@main.route('/', methods = ['GET','POST'])
def index():
    form = BlogForm()
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
   
    return render_template('home.html', title = title, blog = blog
   ,BlogForm = form)
    


@main.route('/blogs/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('blogs.html',form=form)




@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = BlogForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', blog_id= blog_id))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html', form = form, comment = all_comments, blog = blog )

@main.route('/blogs')
def blogs():
    form=CommentForm()

    return render_template("blogs.html",form=form)

@main.route('/write')
def write():
    form=BlogForm()

    return render_template("writer.html",form=form)



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

