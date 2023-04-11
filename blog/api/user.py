from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.permissions.user import UserPermission
from blog.schemas import UserSchema
from blog.models.models import db
from blog.models import Users


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": Users,
        "permission_get": [UserPermission],
        "permission_patch": [UserPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": Users,
    }
