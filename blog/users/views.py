from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models.models import Users

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'David', 2: 'Saymon', 3: 'Bryan'}



@user.route('/')
def user_list():
    users = Users.query.all()
    return render_template('users/list.html', data=users)

@login_required
@user.route('/<int:pk>')
def profile(pk: int):
    _user = Users.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f"User #{_user} doesn't exist!")
    return render_template('users/profile.html', user_name=_user.username)
