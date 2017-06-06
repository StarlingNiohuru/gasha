import os

from app import create_app, db, db_mongo
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app.main.models import Entry

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, db_mongo=db_mongo, User=User, Role=Role, Entry=Entry)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
