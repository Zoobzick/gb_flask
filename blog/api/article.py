from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.schemas import ArticleSchema
from blog.models import Articles
from blog.models.models import db


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
    }
