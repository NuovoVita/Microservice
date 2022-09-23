from ..base import BaseSplitTableModel
from ..extend import db


class UserTpl(BaseSplitTableModel):
    pre_tab_name = 'user'

    @classmethod
    def get_tab_attr(cls):
        return {
            '__bind_key__': cls.__bind_key__,
            '__tablename__': None,
            '__table_args__': {'extend_existing': True},
            'id': db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment=u'编号'),
            'name': db.Column(db.String(30), comment=u'姓名'),
            'gender': db.Column(db.String(10), comment=u'性别'),
            'birth': db.Column(db.Date, comment=u'出生日期'),
        }

    @classmethod
    def to_json(cls, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'gender': instance.gender,
            'birth': str(instance.birth),
        }
