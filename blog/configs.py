import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:vlad72kbhjqrjJ!@localhost:3306/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a%8g)$xp+&2tq15b#=#(-96a6b!4i$0$js_1*m#e7hrqq=ik9='


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True
