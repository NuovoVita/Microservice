import calendar
import logging
import threading
import traceback
from datetime import datetime

from ..extend import db

TAB_CLS_MAPPING = {}
DB_LOCK = threading.Lock()


class BaseSplitTableModel(object):
    base_model = db.Model
    __bind_key__ = 'Microservice'
    pre_tab_name = 'base'

    @classmethod
    def get_month_abbr(cls, month=False):
        if month:
            return calendar.month_abbr[month].lower()
        return calendar.month_abbr[datetime.now().month].lower()

    @classmethod
    def get_tab_lst(cls, bind_key=None, prefix=None, suffix=None):
        if bind_key:
            engine = db.get_engine(bind=bind_key)
        else:
            engine = db.get_engine(bind=cls.__bind_key__)
        tab_lst = map(str, engine.table_names())
        if prefix:
            tab_lst = filter(lambda x: x.startswith(prefix), tab_lst)

        if suffix:
            tab_lst = filter(lambda x: x.endswith(suffix), tab_lst)
        return tab_lst

    @classmethod
    def get_cur_tab_lst(cls, bind_key=None, suffix_name=None):
        suffix = cls.get_month_abbr()
        if suffix_name:
            suffix = suffix_name

        return cls.get_tab_lst(bind_key, cls.pre_tab_name, suffix)

    @classmethod
    def get_tab(cls, suffix=None):
        if not suffix:
            suffix = cls.get_month_abbr()
        return '_'.join([cls.pre_tab_name, suffix])

    @classmethod
    def get_tab_attr(cls):
        return {}

    @classmethod
    def tab_exist(cls, bind_key=None, name=None):
        if name and name in cls.get_tab_lst(bind_key):
            return True
        return

    @classmethod
    def gen_model(cls, bind_key=None, tab_name=None):
        if not tab_name:
            return

        with DB_LOCK:
            tab_name = str(tab_name)
            if tab_name not in TAB_CLS_MAPPING:
                tab_attr = cls.get_tab_attr()
                if bind_key:
                    tab_attr['__bind_key__'] = bind_key
                tab_attr['__tablename__'] = tab_name
                tab_model = type(tab_name, (cls.base_model,), tab_attr)
                if tab_name not in cls.get_tab_lst(bind_key):
                    try:
                        db.create_all()
                        db.session.commit()
                    except Exception as e:
                        logging.error('Err msg is {}'.format(e))
                        logging.error(traceback.format_exc())
                TAB_CLS_MAPPING[tab_name] = tab_model
                return tab_model
            return TAB_CLS_MAPPING[tab_name]
