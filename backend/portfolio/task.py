#from celery.task.schedules import crontab
#from celery.decorators import periodic_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger
import datetime
from celery import task

logger = get_task_logger(__name__)
# @periodic_task(
#     run_every=(crontab(minute='*')), #run task every m
#     name="some_task",
#     ignore_result=True
#     )
# @periodic_task(run_every=datetime.timedelta(seconds=30))


@task()
def some_task():
    # do something
    print("working")
    logger.info("doing task")
