# from app import db
# class User(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     nickname=db.Column(db.String(64),index=True,unique=True)
#     email=db.Column(db.String(120),index=True,unique=True)
#
#     def __repr__(self):
#         return '<User %r>'%(self.nickname)


# from flask import Flask
# import os
# from app import db
# app=Flask(__name__)
# basedir=os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

# from app import db
# class User(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     nickname=db.Column(db.String(64),index=True,unique=True)
#     email=db.Column(db.String(120),index=True,unique=True)
#     posts=db.relationship('Post',backref='author',lazy='dynamic')
#     def __repr__(self):
#         return '<User %r>'%(self.nickname)
#
# class Post(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     body=db.Column(db.String(140))
#     timestamp=db.Column(db.DateTime)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
#     def __repr__(self):
#         return '<Post %r>'%(self.body)

from app import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nickname=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(120),unique=True)
    posts=db.relationship('Post',backref='author',lazy='dynamic')

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
    def __repr__(self):
        return '<User %r>' % (self.nickname)
