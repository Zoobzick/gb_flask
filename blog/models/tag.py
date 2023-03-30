from sqlalchemy.orm import relationship

from blog.models.models import article_tag_association_table
from blog.models.models import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, default="", server_default="")
    articles = relationship(
        "Articles",
        secondary=article_tag_association_table,
        back_populates="tags",
    )

