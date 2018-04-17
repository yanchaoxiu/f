CSRF_ENABLED = True
SECRET_KEY = '123456'


SERVER_KEY='you will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


import os
basedir=os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'db_repository')


# email server
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 0
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('yanchaoxiu@163.com')
MAIL_PASSWORD = os.environ.get('123qwe')

# administrator list
ADMINS = ['yanchaoxiu@163.com']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS=50


