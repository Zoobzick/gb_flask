import os

from blog.app import create_app
from blog.models.models import db, Users

app = create_app()

app.run(
    host="0.0.0.0",
    debug=True
)


# @app.cli.command('init-db')
# def init_db():
#     with app.app_context():
#         db.create_all()
#         print('DB created')


@app.cli.command('create-admin')
def create_admin():
    with app.app_context():
        admin = Users(username='root', email='root@email.com',
                      is_staff=True)
        admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

        db.session.add(admin)
        db.session.commit()

        print('Created admin', admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
        ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")

