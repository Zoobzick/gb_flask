from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import UserSchema
from blog.models.models import db
from blog.models import Users


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": Users,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": Users,
    }
