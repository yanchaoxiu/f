# coding:utf-8
# from app import app
# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello,World"
#
# @app.route('/test')
# def test():
#     return 'this is response'
# def test1():
#     return 'this is response1'
# app.add_url_rule('/test1',view_func=test1)


# # hello,Miguel!
# from flask import render_template
# from app import app
# @app.route('/')
# def index():
#     user={'nickname':'Miguel'}
#     #index.html:hello,{{user.nickname}}!
#     return render_template("index.html",title='Home',user=user)




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
#     return render_template("index.html",title='Home',user=user,posts=posts)


# from flask import url_for,flash,redirect,render_template
# from app import app
# #导入定义的BaseLogin
# from app.forms import BaseLogin
#
# #定义处理函数和路由规则，接收GET和POST请求
# @app.route('/baselogin',methods=('POST','GET'))
# def baselogin():
#     form=BaseLogin()
#     #判断是否是验证提交
#     if form.validate_on_submit():
#         #跳转
#         flash(form.name.data+'|'+form.password.data)
#         return redirect(url_for('success'))
#     else:
#         #渲染
#         return render_template('baselogin.html',form=form)
#
# @app.route('/success')
# def success():
#     return '<h1>Success</h1>'



from app import app, db, lm, models,oid
from flask import render_template, flash, redirect, url_for, session, request, g
from .forms import LoginForm, EditForm,PostForm,SearchForm
from .models import User,Post
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from config import POSTS_PER_PAGE,MAX_SEARCH_RESULTS
from emails import follower_notification
from app import babel
from config import LANGUAGES
from flask_babel import gettext
from guess_language import guessLanguage
from flask import jsonify
from translate import microsoft_translate


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = get_locale()


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body = form.post.data,
            timestamp = datetime.utcnow(),
            author = g.user,
            language = language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Your post is now live!'))
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
        title = 'Home',
        form = form,
        posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if models.User.query.filter_by(nickname=form.openid.data).first():
            user = User.query.filter_by(nickname=form.openid.data).first_or_404()
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html',
                                   title='Sign In',
                                   error='[NO]',
                                   form=form)
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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


@app.route('/edit',methods=["POST","GET"])
@login_required
def edit():
    form=EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname=form.nickname.data
        g.user.about_me=form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved!')
        return redirect(url_for('user',nickname=g.user.nickname))
    else:
        form.nickname.data=g.user.nickname
        form.about_me.data=g.user.about_me
    return render_template('edit.html',form=form)

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

    nickname = User.make_valid_nickname(nickname)
    nickname = User.make_unique_nickname(nickname)
    user = User(nickname = nickname, email = resp.email, role = ROLE_USER)

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
    follower_notification(user, g.user)
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

@app.route('/search', methods = ['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query = g.search_form.search.data))

@app.route('/search_results/<query>')
@login_required
def search_results(query):
    results = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
        query = query,
        results = results)

@babel.localeselector
def get_locale():
    return "es" #request.accept_languages.best_match(LANGUAGES.keys())


@app.route('/translate', methods = ['POST'])
@login_required
def translate():
    return jsonify({
        'text': microsoft_translate(
            request.form['text'],
            request.form['sourceLang'],
            request.form['destLang']) })




