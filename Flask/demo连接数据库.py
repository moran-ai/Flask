from flask_script import Manager
from apps import create_app
from flask_migrate import Migrate, MigrateCommand
from ext import db
# 导入模型
from apps.user.models import User

# 构建app对象
app = create_app()
# 将manager与app相关联
manager = Manager(app=app)

# 配置migrate
# 影响数据库的映射/迁移 两个参数，一个是app, 一个是数据库db
migrate = Migrate(app=app, db=db)

# 将命令交给manager管理 添加命令,命令的名字是db, 并和MigrateCommand进行绑定
manager.add_command('db', MigrateCommand)

@manager.command
def init():
    """
    自定义命令
    :return:
    """
    print('初始化')

if __name__ == '__main__':
    manager.run()
