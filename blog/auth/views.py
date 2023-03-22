from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, LoginManager, login_user
from werkzeug.security import check_password_hash

from blog.models.models import Users
from flask_login import login_required
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


auth = Blueprint('auth', __name__, static_folder='../static')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your input details')
        return redirect(url_for('.login'))
    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_manager.user_loader
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"
