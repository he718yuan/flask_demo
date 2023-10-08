from flask import Blueprint,render_template,redirect,url_for,session
from flask import request
from exts import db
from .forms import RegisterForm,LoginForm
from models import ManagerModel
from werkzeug.security import generate_password_hash,check_password_hash
# url前缀：/auth
bp = Blueprint("auth",__name__,url_prefix="/auth")


@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = ManagerModel.query.filter_by(username=username).first()
            if not user:
                print("数据在数据库中不存在！")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie:
                # cookie中不适合存储太多的数据，只适合存储少量数据
                # cookie一般用来存放登录授权的东西
                # flask中的session，是经过加密后存储在cookie中
                session['user_id'] = user.id
                return redirect(url_for("qa.index"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# get：从服务器上获取数据
# past：将客户端的数据提交给服务器
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # 表单验证：flask-wtf:wtforms
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = ManagerModel(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # return redirect("/auth/login")
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")