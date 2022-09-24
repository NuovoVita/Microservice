# -*- coding: utf-8 -*-
import logging.config
import os
import pathlib

from flask import Flask

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
PROFILE = os.getenv('PROFILE', 'prod')
logger = None


class MicroserviceMain:
    _URL_PREFIX = '/api'

    @classmethod
    def _init_log(cls, profile=None):
        global logger
        if not profile:
            profile = os.getenv('PROFILE', 'prod')
        log_conf = PROJECT_ROOT.joinpath('conf').joinpath('logging.conf')
        logging.config.fileConfig(log_conf)
        logger = logging.getLogger(profile)

    @classmethod
    def _init_settings(cls, app, profile=None, config_file=None):
        if config_file:
            app.config.from_pyfile(config_file)
            return

        if not profile:
            profile = os.getenv('PROFILE', 'prod')

        from conf import config
        app.config.from_object(config[profile])

    @classmethod
    def _register_views(cls, app):
        from .user import user_bp
        app.register_blueprint(user_bp, url_prefix=cls._URL_PREFIX)

    @classmethod
    def _init_extensions(cls, app):
        from .extend import db
        db.init_app(app)

    @classmethod
    def create_app(cls, profile=None, config_file=None):
        cls._init_log(profile)
        _app = Flask(__name__)
        cls._init_settings(_app, profile, config_file)
        cls._init_extensions(_app)
        cls._register_views(_app)
        return _app
