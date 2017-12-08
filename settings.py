# -*- coding: utf-8 -*-

class Config:
    DEBUG = False

class DevelopConfig:
    DEBUG = True
    SQLAlCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/test1"
