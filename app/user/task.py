from worker.celery_app import celery, logger
from wsgi import app
from .model import UserTpl


@celery.task
def count_user_number_task():
    with app.app_context():
        tab_name = UserTpl.get_tab()
        tab_model = UserTpl.gen_model(app.config['BASE_DB_NAME'], tab_name)
        count = tab_model.query.count()
        logger.info(count)
    logger.info('Finish count-user-task.')
