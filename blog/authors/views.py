from flask import Blueprint, render_template
from blog.models.models import Author

author = Blueprint("author", __name__, url_prefix="/authors")


@author.route("/", endpoint="list")
def author_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)
