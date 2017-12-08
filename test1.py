# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# 模型类关联
from models import db
db.init_app(app)

from settings import *
app.config.from_object(DevelopConfig)

# 拓展命令包
from flask_script import Manager
manager = Manager(app)

# 迁移命令
from flask_migrate import Migrate, MigrateCommand
# 初始化迁移对象
Migrate(app, db)

# 添加db命令， 执行命令时会调用MigrateCommand执行
manager.add_command("db", MigrateCommand)





@app.route("/")
def hello_flask():
    return "hello flask!"

if __name__ == "__main__":
    manager.run()
