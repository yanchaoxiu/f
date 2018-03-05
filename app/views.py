# from app import app
# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello,xiu"

# from flask import render_template,flash,redirect
# from app import app
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     return render_template('login.html',title='Sign In',form=form)
# app.run(debug=True)

from flask import render_template,flash,redirect
from app import app
from forms import LoginForm
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="'+(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form)
app.run(debug=True)
