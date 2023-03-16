from flask import Blueprint, render_template

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

articles = {
    1: {
        'title': 'lorem1',
        'text': 'text1',
        'author': {
            'name': 'David',
            'id': 1
        }
    },
    2: {
        'title': 'lorem2',
        'text': 'text2',
        'author': {
            'name': 'Saymon',
            'id': 2
        }
    },
    3: {
        'title': 'lorem3',
        'text': 'text3',
        'author':{
            'name': 'Bryan',
            'id': 3
        }
    }
}

@article.route('/')
def articles_list():
    return render_template('articles/list.html', articles=articles)


@article.route('/<int:pk>')
def get_article(pk: int):
    article = articles[pk]
    return render_template('articles/details.html', article=article)