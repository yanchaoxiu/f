from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid=StringField('openid',validators=[DataRequired()])
    remember_me=BooleanField('remember_me',default=False)



from flask_wtf import Form
from wtforms import StringField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length

# class EditForm(Form):
#     nickname=StringField('nickname',validators=[DataRequired()])
#     about_me=TextAreaField('about_me',validators=[Length(min=0,max=140)])


from models import User
class EditForm(Form):
    nickname=StringField('nickname',validators=[DataRequired()])
    about_me=TextAreaField('about_me',validators=[Length(min=0,max=140)])
    def __init__(self,original_nickname,*args,**kwargs):
        Form.__init__(self,*args,**kwargs)
        self.original_nickname=original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data==self.original_nickname:
            return True
        user=User.query.filter_by(nickname=self.nickname.data).first()
        if user !=None:
            self.nickname.errors.append('this nickname is already in use.please choose another one')
            return False
        return True


class PostForm(Form):
    post=StringField('post',validators=[DataRequired()])