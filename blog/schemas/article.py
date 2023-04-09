from combojsonapi.utils import Relationship
from marshmallow_jsonapi import fields, Schema


class ArticleSchema(Schema):
    class Meta:
        type_ = "Article"
        self_view = "article_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "article_list"

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False)
    text = fields.String(allow_none=False)
    date_created = fields.DateTime(allow_none=False)
    date_updated = fields.DateTime(allow_none=False)

    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_url="author_detail",
        related_url_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )
    tags = Relationship(
        nested="TagSchema",
        attribute="tags",
        related_view="tag_detail",
        related_view_kwargs={"id": "<id>"},
        schema="TagSchema",
        type_="tag",
        many=True,
    )
