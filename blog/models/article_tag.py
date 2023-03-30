from blog.models.models import db


article_tag_association_table = db.Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, db.ForeignKey("articles.id"), nullable=False),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), nullable=False),
    )
