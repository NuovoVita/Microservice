import random

from flask import Blueprint, jsonify, request, current_app

from .model import UserTpl
from ..extend import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/user', methods=['GET'])
def show_user():
    page = request.args.get('page', 1, int)
    page_size = request.args.get('size', 10, int)
    tab_name = UserTpl.get_tab()
    tab_model = UserTpl.gen_model(current_app.config['BASE_DB_NAME'], tab_name)

    user_obj = tab_model.query.paginate(
        page=page, per_page=page_size
    )
    user_lst = []
    for user in user_obj.items:
        user_lst.append(UserTpl.to_json(user))
    return jsonify(
        {
            'result': True,
            'data': user_lst,
            'total': user_obj.total,
            'message': 'OK'
        }
    )


@user_bp.route('/save-user', methods=['POST'])
def save_user():
    from faker import Faker
    fake = Faker()
    all_gender = ['male', 'female']

    def answer1(count=1000):
        for _ in range(count):
            instance = tab_model(
                name=fake.name(),
                gender=random.choices(all_gender)[0],
                birth=str(fake.date_of_birth())
            )
            db.session.add(instance)
        db.session.commit()

    def answer2(count=1000):
        db.session.bulk_save_objects(
            [
                tab_model(name=fake.name(), gender=random.choices(all_gender)[0], birth=str(fake.date_of_birth()))
                for _ in range(count)
            ]
        )
        db.session.commit()

    def answer3(count=1000):
        db.session.bulk_insert_mappings(
            tab_model,
            [
                dict(name=fake.name(), gender=random.choices(all_gender)[0], birth=str(fake.date_of_birth()))
                for _ in range(count)
            ]
        )
        db.session.commit()

    def answer4(count=1000):
        db.session.execute(
            tab_model.__table__.insert(),
            [
                dict(name=fake.name(), gender=random.choices(all_gender)[0], birth=str(fake.date_of_birth()))
                for _ in range(count)
            ]
        )
        db.session.commit()

    answer_function_mapping = {
        'Answer1': answer1,
        'Answer2': answer2,
        'Answer3': answer3,
        'Answer4': answer4,
    }

    params = request.get_json()
    if not params or 'method' not in params:
        return jsonify({'result': False, 'data': None, 'message': u'参数异常'})

    if params['method'] not in answer_function_mapping:
        return jsonify({'result': False, 'data': None, 'message': u'method = {}， 参数异常'.format(params['method'])})

    gen_count = params.get('count', 100)
    tab_name = UserTpl.get_tab()
    tab_model = UserTpl.gen_model(current_app.config['BASE_DB_NAME'], tab_name)

    answer_function = answer_function_mapping[params['method']]
    answer_function(gen_count)
    return jsonify(
        {
            'message': f'Answer1 - Answer4 性能依次增強'
        }
    )
