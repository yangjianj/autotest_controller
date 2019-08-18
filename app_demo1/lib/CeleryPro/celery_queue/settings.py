# -*- coding: utf-8 -*-
from kombu import Exchange, Queue

# queue_1与queue_2为消息队列名称
# Exchange:为交换机实例，具有不同的类型。详细参考
# routing_key:用来告知exchange将task message传送至相对应的queue
CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('app_q1', exchange=Exchange('Exchange1', type='direct'), routing_key='app_task1'),
    Queue('app_q2', exchange=Exchange('Exchange1', type='direct'), routing_key='app_task2'),
)

CELERY_ROUTES = {
    'mycelery.test_queue_1': {'queue': 'app_q1', 'routing_key': 'app_task1'},
    'mycelery.test_queue_2': {'queue': 'app_q2', 'routing_key': 'app_task2'}
}

c_broker="redis://127.0.0.1:6379/0"
c_backend="redis://127.0.0.1:6379/0"