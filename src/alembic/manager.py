from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.models import db
from src.app import app

MIGRATION_DIR = f'./src/alembic/migrations'

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
