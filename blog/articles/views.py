from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.forms.article import CreateArticleForm
from blog.models import Tag
from blog.models.models import Articles, db, Author

import requests

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@article.route("/", endpoint="list")
def article_list():
    articles = Articles.query.all()
    print(articles)
    return render_template("articles/list.html", articles=articles)


@article.route("/<int:article_id>/", endpoint="details")
def article_details(article_id):
    article = Articles.query.filter_by(id=article_id).options(joinedload(Articles.tags)).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)


@article.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        article = Articles(title=form.title.data.strip(), text=form.text.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article")
            error = "Could not create article"
        else:
            return redirect(url_for("articles.details", article_id=article.id))

    return render_template("articles/create.html", form=form, error=error)


@article.route("/api_data/", endpoint="api_data")
def article_api_data_list():
    response = requests.get("http://127.0.0.1:5000/api/articles/?include=author&fields%5Bauthor%5D=user").json()['data']
    print(response)
    return render_template("articles/api_data.html", articles=response)
