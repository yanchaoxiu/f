from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app.config.from_object('config')
app.config['SECRET_KEY'] = 'mtianyan_movie'
db=SQLAlchemy(app)


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

Im=LoginManager()
Im.init_app(app)
oid=OpenID(app,os.path.join(basedir,'tmp'))
Im.login_view='login'