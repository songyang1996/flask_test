# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
# 数据库对象
db =SQLAlchemy()

class Author(db.Models):
    "作者类"
    __tablename__ = "authors"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(32), primary_key=True)  # 作者姓名

class Book(db.Model):
    "图书类"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(32), unique=True)  # 书名
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))  # 对应的作者名
