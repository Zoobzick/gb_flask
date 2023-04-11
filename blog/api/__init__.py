from flask_combo_jsonapi import Api

from blog.api.author import AuthorList, AuthorDetail
from blog.api.tag import TagList, TagDetail
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from blog.api.article import ArticleList, ArticleDetail
from blog.api.user import UserList, UserDetail


def create_api_spec_plugin(app):
    app.config['OPENAPI_URL_PREFIX'] = '/api/swagger'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_VERSION'] = '3.22.0'
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    event_plugin = EventPlugin(app)
    permission_plugin = PermissionPlugin(strict=False)
    api = Api(
        app,
        plugins=[api_spec_plugin,
                 event_plugin,
                 permission_plugin])

    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>", tag="Article")
