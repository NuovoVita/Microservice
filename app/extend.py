# -*- coding: utf-8 -*-
import pymysql

# from flask_cors import CORS
# from flask_login import LoginManager
# from flask_migrate import Migrate
# from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

# cors = CORS()
# lm = LoginManager()
db = SQLAlchemy()
# redis = FlaskRedis()
# migrate = Migrate()
# CACHE = Cache.instance()
