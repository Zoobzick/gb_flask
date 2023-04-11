

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql://root@https://gb-flask-ycuz.onrender.com:3306/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a%8g)$xp+&2tq15b#=#(-96a6b!4i$0$js_1*m#e7hrqq=ik9='
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    # OPENAPI_SWAGGER_UI_PATH = '/'
    # OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root@https://gb-flask-ycuz.onrender.com:3306/blog"
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
