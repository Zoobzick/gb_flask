from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.models import db, Users

app = create_app()

@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.create_all()
        print('DB created')


@app.cli.command('create-users')
def create_users():
    with app.app_context():
        admin = Users(username='root', email='root@email.com', is_staff=True, password=generate_password_hash('test'))
        client = Users(username='trv', email='trv@mail.ru', is_staff=False, password=generate_password_hash('test1'))
        db.session.add(admin)
        db.session.add(client)
        db.session.commit()
        print('Done, users created')
