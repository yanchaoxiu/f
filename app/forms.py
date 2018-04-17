#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length
from models import User

__author__ = 'kikay'

#登录表单类,继承与Form类
class BaseLogin(FlaskForm):
    #用户名
    name=StringField('name',validators=[DataRequired(message=u"用户名不能为空")
        ,Length(10,20,message=u'长度位于10~20之间')],render_kw={'placeholder':u'输入用户名'})
    #密码
    password=PasswordField('password',validators=[DataRequired(message=u"密码不能为空")
        ,Length(10,20,message=u'长度位于10~20之间')],render_kw={'placeholder':u'输入密码'})


from wtforms import StringField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    # TextAreaField( )是多行文本输入
    # validators=[Length(min=0,max=140)],validators过滤器，输入最小0，最大140
    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class PostForm(FlaskForm):
    post = StringField('post', validators=[DataRequired()])

class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])


# from models import User
# class EditForm(Form):
#     nickname=StringField('nickname',validators=[DataRequired()])
#     about_me=TextAreaField('about_me',validators=[Length(min=0,max=140)])
#     def __init__(self,original_nickname,*args,**kwargs):
#         Form.__init__(self,*args,**kwargs)
#         self.original_nickname=original_nickname
#
#     def validate(self):
#         if not Form.validate(self):
#             return False
#         if self.nickname.data==self.original_nickname:
#             return True
#         user=User.query.filter_by(nickname=self.nickname.data).first()
#         if user !=None:
#             self.nickname.errors.append('this nickname is already in use.please choose another one')
#             return False
#         return True
#
#
# class PostForm(Form):
#     post=StringField('post',validators=[DataRequired()])