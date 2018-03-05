from flask import Flask
from flask.views import View
from app import app
app=Flask(__name__)
app.config.from_object('config')
