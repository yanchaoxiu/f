

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



from flask import render_template,flash,redirect
from app import app
import config
from forms import LoginForm
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="123'+form.openid.data+'123",remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login1.html',title='Sign In',form=form)
app.run(debug=True)

# from flask import render_template,flash,redirect,session,url_for,request,g
# from flask_login import login_user,logout_user,current_user,login_required
# from app import app,db,Im,oid
# from forms import LoginForm
# from models import User
#
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
