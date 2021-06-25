from flask import Flask
from apps import creat_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.model import User
from exts import db

app = creat_app()

# 将manager与app对象相关联
manager = Manager(app=app)

# 配置migrate
migrate = Migrate(app=app, db=db)

# 添加命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
