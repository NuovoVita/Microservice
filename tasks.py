from invoke import task


@task
def run(c, debug=True, flag=None, port=8000):
    if debug:

        if flag == 'server':
            c.run(f'python manage.py runserver 0:{port}')
        elif flag == 'worker':
            c.run('celery -A RobotDetection worker -c 100 -P gevent -l DEBUG')
        elif flag == 'beat':
            c.run('celery -A RobotDetection.celery beat -l DEBUG -s /tmp/celerybeat-schedule')
        else:
            print('Error: Invalid parameter')
    else:
        if flag == 'server':
            c.run(f'python manage.py runserver 0:{port} --noreload')
        elif flag == 'worker':
            c.run('celery -A RobotDetection worker -c 100 -P gevent -l INFO')
        elif flag == 'beat':
            c.run('celery -A RobotDetection.celery beat -l INFO -s /tmp/celerybeat-schedule')
        else:
            print('Error: Invalid parameter')


@task
def init_db(c):
    c.run("python manager.py drop_all")
    c.run("python manager.py create_all")
    c.run("python manager.py init_base_data")


@task
def dev(c):
    c.run("python manager.py drop_all")
    c.run("python manager.py create_all")
    c.run("python manager.py init_base_data")
    c.run("python manager.py init_device_data")
    c.run("python manager.py insert_test_data")


@task
def clean_es(c):
    c.run("python manager.py clean_es_data")
