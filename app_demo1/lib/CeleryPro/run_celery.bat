celery -A task1 worker --loglevel=info -P eventlet
celery -A task worker --loglevel=debug -P eventlet

#指定broker队列
celery -A mycelery worker -l info -Q app_q1 -P eventlet

多个broker工作时，会安排空闲的broker工作