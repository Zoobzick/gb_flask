from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship
from blog.security.security import flask_bcrypt

db = SQLAlchemy()

article_tag_association_table = db.Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, db.ForeignKey("articles.id"), nullable=False),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), nullable=False),
)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    _password = db.Column(db.LargeBinary, nullable=False)
    author = relationship("Author", uselist=False, back_populates="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)


class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="articles")
    date_created = db.Column(db.DateTime, server_default=func.now())
    date_updated = db.Column(db.DateTime, onupdate=func.now())
    tags = relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="articles",
    )

    def __str__(self):
        return self.title


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = relationship("Users", back_populates="author")
    articles = relationship("Articles", back_populates="author")

    def __str__(self):
        return self.user.username
