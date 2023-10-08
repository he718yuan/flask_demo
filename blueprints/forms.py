import wtforms
from wtforms.validators import Length, EqualTo


# Form：主要是用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=1, max=20, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=1, max=20, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])


class UserForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=1, max=20, message="用户名格式错误！")])
    sex = wtforms.StringField(validators=[Length(min=1, max=10, message="格式错误！")])
    tel = wtforms.StringField(validators=[Length(min=8, max=12, message="格式错误！")])
    live = wtforms.StringField(validators=[Length(min=1, max=10, message="格式错误！")])
