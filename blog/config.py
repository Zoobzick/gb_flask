import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://trv:password@localhost:5432/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a%8g)$xp+&2tq15b#=#(-96a6b!4i$0$js_1*m#e7hrqq=ik9='
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root:vlad72kbhjqrjJ!@localhost:3306/blog"
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
