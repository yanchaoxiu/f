# coding:utf-8
# sqlalchemy 连接 sqlite
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///D:/blog/app/app.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    nickname=db.Column(db.String(64),unique=True,index=True)
    email=db.Column(db.String(120),unique=True,index=True)
    def __repr__(self):
        return '<User %r>' % (self.nickname)


# class User(db.Model):
#     __tablename__='posts'
#     id=db.Column(db.Integer,primary_key=True)
#     body=db.Column(db.String(140),unique=True,index=True)
#     timestamp=db.Column(db.DateTime,index=True)
#     user_id=db.Column(db.Integer,index=True)

# class User(db.Model):
#     __tablename__='students'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.Integer,index=True)

# class User(db.Model):
#     __tablename__='teachers'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.Integer,index=True)

# class User(db.Model):
#     __tablename__='student_teacher'
#     student_id=db.Column(db.Integer,primary_key=True)
#     teacher_id = db.Column(db.Integer,index=True)

# class User(db.Model):
#     __tablename__='followers'
#     follow_id=db.Column(db.Integer,primary_key=True)
#     followed_id = db.Column(db.Integer,index=True)
#
db.create_all()


# from models import Post
# from app import db
# for post in Post.query.all():
#     db.session.delete(post)
# db.session.commit()