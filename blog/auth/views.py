from flask import Blueprint, current_app, render_template, request, flash, redirect, url_for
from flask_login import current_user, logout_user, LoginManager, login_user
from werkzeug.security import check_password_hash
from werkzeug.exceptions import NotFound

from blog.models.models import db
from blog.forms.user import LoginForm, RegistrationForm
from blog.models.models import Users
from flask_login import login_required

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect("articles.articles_list")
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = Users.query.filter_by(
            username=form.username.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="username doesn't exist")
        if not user.validate_password(form.password.data):
            return render_template("auth/login.html", form=form, error="invalid username or password")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)

    # if request.method == 'GET':
    #     return render_template('auth/login.html')
    # email = request.form.get('email')
    # password = request.form.get('password')

    # user = Users.query.filter_by(email=email).first()

    # if not user or not check_password_hash(user.password, password):
    #     flash('Check your input details')
    #     return redirect(url_for('.login'))
    # login_user(user)
    # return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout/')
@login_manager.user_loader
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"


@auth.route("/register/", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("articles.articles_list"))
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if Users.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)
        if Users.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = Users(
            username=form.username.data,
            email=form.email.data,
            is_staff=False)
        user.password = form.password.data
        db.session.add(user)

        try:
            db.session.commit()
        except IntegirtyError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("index"))

    return render_template("auth/register.html", form=form, error=error)


@auth.route("/login-as", methods=["GET", "POST"], endpoint="login-as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound
        # non-admin users
