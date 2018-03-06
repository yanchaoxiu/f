from flask import Flask

app = Flask(__name__)

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

Im=LoginManager()
Im.init_app(app)
oid=OpenID(app,os.path.join(basedir,'tmp'))
Im.login_view='login'