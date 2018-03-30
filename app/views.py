

# # hello,Miguel!
# from flask import render_template
# from app import app
# @app.route('/')
# def index():
#     user={'nickname':'Miguel'}
#     #index.html:hello,{{user.nickname}}!
#     return render_template("index.html",title='Home',user=user)
# app.run(debug=True)



# # Hello,Miguel!
# from flask import Flask,render_template
# from app import app
# @app.route('/')
# def index():
#     user={'nickname':'Miguel'}
#     posts=[ # fake array of posts
#         {
#             'author':{'nickname':'join'},
#             'body':'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     # {% if title %} {% else %} {% endif %}
#     # Hello,{{user.nickname}}!
#     return render_template("index1.html",title='Home',user=user,posts=posts)
# app.run(debug=True)


# # Hi,Miguel!
# # join says: Beautiful day in Portland!
# # Susan says: The Avengers movie was so cool!
# from flask import Flask,render_template
# from app import app
# @app.route('/')
# def index():
#     user={'nickname':'Miguel'}
#     posts=[ # fake array of posts
#         {
#             'author':{'nickname':'join'},
#             'body':'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     # { % if title %} { % else %} { % endif %}
#     # Hi, {{user.nickname}}!
#     #
#     # { %
#     # for post in posts %}
#     # {{post.author.nickname}}
#     # says: {{post.body}}
#     #
#     # { % endfor %}
#     return render_template("index2.html",title='Home',user=user,posts=posts)
# app.run(debug=True)



# from flask import Flask,render_template
# from app import app
# @app.route('/')
# def index():
#     user={'nickname':'Miguel'}
#     posts=[ # fake array of posts
#         {
#             'author':{'nickname':'join'},
#             'body':'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index3.html",title='Home',user=user,posts=posts)
# app.run(debug=True)


# from flask import render_template,flash,redirect
# from app import app
# import config
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     return render_template('login.html',title='Sign In',form=form)
# app.run(debug=True)

# from flask import render_template,flash,redirect
# from app import app
# import config
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="123'+form.openid.data+'123",remember_me='+str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html',title='Sign In',form=form)
# app.run(debug=True)



# from flask import render_template,flash,redirect
# from app import app
# import config
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="123'+form.openid.data+'123",remember_me='+str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login1.html',title='Sign In',form=form)
# app.run(debug=True)



# from flask import Flask,flash,redirect,render_template
# from app import app
# import config
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         flash('login requested for OpenID="'+
#               form.openid.data+'",remember_me='+
#               str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login2.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])
# app.run(debug=True)






# from flask import render_template,flash,redirect,session,url_for,request,g,Flask,render_template
# from flask_login import logout_user,login_user,current_user,login_required
# from app import app,db,Im,oid
# from forms import LoginForm
# from models import User
# from datetime import datetime
# from app import Im
# from models import User
# @Im.user_loader
# def load_user(id):
#     return User.query.get(int(id))
# @app.route('/login',methods=['GET','POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('index'))
#     form=LoginForm()
#     if form.validate_on_submit():
#         session['remember_me']=form.remember_me.data
#         return oid.try_login(form.openid.data,ask_for=['nickname','email'])
#     return render_template('login2.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])
# @oid.after_login
# def after_login(resp):
#     if resp.email is None or resp.email==" ":
#         flash('Invalid login. Please try again.')
#         return redirect(url_for('login'))
#     user=User.query.filter_by(email=resp.email).first()
#     if user is None:
#         nickname=resp.nickname
#         if nickname is None or nickname==" ":
#             nickname=resp.email.split('@')[0]
#         user=User(nickname=nickname,email=resp.email)
#         db.session.add(user)
#         db.session.commit()
#     remember_me=False
#     if 'remember_me'in session:
#         remember_me=session['remember_me']
#         session.pop('remember_me',None)
#     login_user(user,remember=remember_me)
#     return redirect(request.args.get('next') or url_for('index'))
# @app.before_request
# def before_request():
#     g.user=current_user
# @app.route('/')
# @app.route('/index')
# @login_required
# def index():
#     user=g.user
#     posts=[
#         {
#             'author':{'nickname':'john'},
#             'body':'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index3.html",title='Home',user=user,posts=posts)
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
# @app.route('/user/<nickname>')
# @login_required
# def user(nickname):
#     user=User.query.filter_by(nickname=nickname).first()
#     if user==None:
#         flash('User'+nickname+'not found.')
#         return redirect(url_for('index'))
#     posts=[
#         {'author':user,'body':'Test post #1'},
#         {'author':user,'body':'Test post #2'}
#     ]
#     return render_template('user.html',user=user,posts=posts)
# app.run(debug=True)



# @app.before_request
# def before_request():
#     g.user=current_user
#     if g.user.is_authenticated:
#         g.user.last_seen=datetime.utcnow()
#         db.session.add(g.user)
#         db.session.commit()

# from forms import LoginForm,EditForm
# from app import app,db
# from flask import g,flash,redirect,url_for,render_template
# from flask_login import login_required
# @app.route('/edit',methods=['GET','POST'])
# @login_required
# def edit():
#     form=EditForm
#     if form.validate_on_submit():
#         g.user.nickname=form.nickname.data
#         g.user.about_me=form.about_me.data
#         db.session.add(g.user)
#         db.session.commit()
#         flash('Your changes have been saved.')
#         return redirect(url_for('edit'))
#     else:
#         form.nickname.data=g.user.nickname
#         form.about_me.data=g.user.about_me
#     return render_template('edit.html',form=form)


# @app.errorhandler(404)
# def internal_error(error):
#     return render_template('404.html'),404
# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html'),500
# from models import User

# #you wen ti
# if user is None
#     nickname=resp.nickname
#     if nickname is None or nickname==" ":
#         nickname=resp.email.split('@')[0]
#     nickname=User.make_unique_nickname(nickname)
#     user=User(nickname=nickname,email=resp.email)
#     db.session.add(user)
#     db.session.commit()

from app import app
from forms import EditForm
from flask_login import login_required
@app.route('/edit',methods=['GET','POST'])
@login_required
def edit():
    form=EditForm(g.user.nickname)

from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user,logout_user,current_user,login_required
from app import app,db,Im,oid
from forms import LoginForm
from models import User

# @app.route('/login',methods=['GET','POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated():
#         return redirect(url_for('index'))
#     form=LoginForm()
#     if form.validate_on_submit():
#         session['remember_me']=form.remember_me.data
#         return oid.try_login(form.openid.data,ask_for=['nickname','email'])
#     return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])
# @oid.after_login
# def after_login(resp):
#     if resp.email is None or resp.email=="":
#         flash('invalid login.please tyr again')
#         return redirect(url_for('login'))
#     user=User.query.filter_by(email=resp.email).first()
#     if user is None:
#         nickname=resp.nickname
#         if nickname is None or nickname=="":
#             nickname=resp.email.sqlit('@')[0]
#             user=User(nickname=nickname,email=resp.email)
#             db.session.add(user)
#             db.session.commit()
#         remember_me=False
#         if 'remember_me' in session:
#             remember_me=session['remember_me']
#             session.pop('remember_me',None)
#         login_user(user,remember=remember_me)
#         return redirect(request.args.get('next') or url_for('index'))
#
#
# @app.before_request
# def before_request():
#     g.user=current_user


def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname = nickname, email = resp.email)
        db.session.add(user)
        db.session.commit()
        # make the user follow him/herself
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


# @app.route('/follow/<nickname>')
# @login_required
# def follow(nickname):
#     user = User.query.filter_by(nickname=nickname).first()
#     if user is None:
#         flash('User %s not found.' % nickname)
#         return redirect(url_for('index'))
#     if user == g.user:
#         flash('You can not follow yourself!')
#         return redirect(url_for('user', nickname=nickname))
#     u = g.user.follow(user)
#     if u is None:
#         flash('Cannot follow ' + nickname + '.')
#         return redirect(url_for('user', nickname=nickname))
#     db.session.add(u)
#     db.session.commit()
#     flash('You are now following ' + nickname + '!')
#     return redirect(url_for('user', nickname=nickname))

# @app.route('/unfollow/<nickname>')
# @login_required
# def unfollow(nickname):
#     user = User.query.filter_by(nickname=nickname).first()
#     if user is None:
#         flash('User %s not found.' % nickname)
#         return redirect(url_for('index'))
#     if user == g.user:
#         flash('You can not unfollow yourself!')
#         return redirect(url_for('user', nickname=nickname))
#     u = g.user.unfollow(user)
#     if u is None:
#         flash('Cannot unfollow ' + nickname + '.')
#         return redirect(url_for('user', nickname=nickname))
#     db.session.add(u)
#     db.session.commit()
#     flash('You have stopped following ' + nickname + '.')
#     return redirect(url_for('user', nickname=nickname))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname = nickname, email = resp.email)
        db.session.add(user)
        db.session.commit()
        # make the user follow him/herself
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash('Cannot follow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You are now following ' + nickname + '!')
    return redirect(url_for('user', nickname=nickname))

@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t unfollow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash('Cannot unfollow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You have stopped following ' + nickname + '.')
    return redirect(url_for('user', nickname=nickname))


# from forms import LoginForm, EditForm, PostForm
# from models import User, Post
# import datetime
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# @login_required
# def index():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(body=form.post.data, timestamp=datetime.utcnow(), author=g.user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post is now live!')
#         return redirect(url_for('index'))
#     posts = [
#         {
#             'author': {'nickname': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index4.html',
#                            title='Home',
#                            form=form,
#                            posts=posts)


from forms import LoginForm, EditForm, PostForm
from models import User, Post
from config import POSTS_PER_PAGE
import datetime
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body = form.post.data, timestamp = datetime.utcnow(), author = g.user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False).items
    return render_template('index4.html',
        title = 'Home',
        form = form,
        posts = posts)


@app.route('/user/<nickname>')
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname, page=1):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = user.posts.paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
                           user=user,
                           posts=posts)
