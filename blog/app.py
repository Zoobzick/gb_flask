from flask import Flask, redirect, url_for

from blog.articles.views import article
from blog.auth.views import auth, login_manager
from blog.models.models import db, Users
from blog.users.views import user
import os





def create_app() -> Flask:
    app = Flask(__name__)

    cfg_name = os.environ.get("CONFIG_NAME") or "Production_config"
    app.config.from_object(f"blog.config.{cfg_name}")
    # app.config['SECRET_KEY'] = 'a%8g)$xp+&2tq15b#=#(-96a6b!4i$0$js_1*m#e7hrqq=ik9='
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:vlad72kbhjqrjJ!@localhost:3306/blog"

    db.init_app(app)

    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(article)


