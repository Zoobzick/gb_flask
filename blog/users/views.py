from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'David', 2: 'Saymon', 3: 'Bryan'}



@user.route('/')
def user_list():
    return render_template('users/list.html', data=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    user_name = USERS[pk]
    return render_template('users/details.html', user_name=user_name)
