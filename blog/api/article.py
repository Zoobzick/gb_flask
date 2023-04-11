from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.permissions.article import ArticlePermissions
from blog.schemas import ArticleSchema
from blog.models import Articles
from blog.models.models import db
from combojsonapi.event.resource import EventsResource


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count:": Articles.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
        "permission_patch": [ArticlePermissions],
        "permission_get": [ArticlePermissions],
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
        # "permission_patch": [ArticlePermissions],
        # "permission_get": [ArticlePermissions],
    }
