from flask import Blueprint, request, render_template, redirect, url_for
from .forms import UserForm
from models import UserModel
from exts import db
from decorators import login_required

bp = Blueprint("qa", __name__, url_prefix="/")


# http://127.0.0.1:5000
@bp.route('/')
@login_required
def index():
    users = UserModel.query.order_by(UserModel.id).all()
    return render_template("index.html", users=users)


@bp.route('/search')
@login_required
def search():
    # 请求参数的三种方式
    # /search?q=flash
    # /search/<q>
    # post, request.form
    q = request.args.get("q")
    users = UserModel.query.filter(UserModel.username.contains(q)).all()
    return render_template("index.html", users=users)


@bp.route('/insert', methods=['GET', 'POST'])
@login_required
def qa_insert():
    if request.method == 'GET':
        return render_template("serach.html")
    else:
        form = UserForm(request.form)
        if form.validate():
            username = form.username.data
            sex = form.sex.data
            tel = form.tel.data
            live = form.live.data
            user = UserModel(username=username, sex=sex, tel=tel, live=live)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for('qa.qa_insert'))


@bp.route('/delete/<qa_id>')
@login_required
def qa_delete(qa_id):
    user = UserModel.query.get(qa_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


@bp.route('/update/<qa_id>', methods=['GET', 'POST'])
@login_required
def qa_update(qa_id):
    if request.method == 'GET':
        user = UserModel.query.get(qa_id)
        return render_template('update.html', user=user)
    else:
        form = UserForm(request.form)
        if form.validate():
            username = form.username.data
            sex = form.sex.data
            tel = form.tel.data
            live = form.live.data
            user = UserModel.query.get(qa_id)
            user.username = username
            user.sex = sex
            user.tel = tel
            user.live = live
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for('qa.qa_update'))
