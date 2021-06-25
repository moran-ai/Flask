from ext import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models.User import User
from apps import create_app

app = create_app()

manager = Manager(app=app)
# 影响数据库的映射
migrate = Migrate(app=app, db=db)
# 将命令交给manager进行管理
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
