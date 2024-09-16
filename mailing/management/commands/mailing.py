import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mailing.models import Mailing
from mailing.services import send_mailing

logger = logging.getLogger(__name__)


@util.close_old_connections
def delete_old_job_executions(max_age=86_400):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def activate_mailing():
    for mail in Mailing.objects.all():
        start_date = mail.departure_date
        mail.activate(start_date)


def scheduler_load(name):
    sched_dict = {'back': BackgroundScheduler, 'block': BlockingScheduler}
    scheduler = sched_dict[name](timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(delete_old_job_executions, 'interval',
                      days=7, id='delete_old_job', replace_existing=True)
    scheduler.add_job(activate_mailing, 'interval',
                      minutes=1, id='activate', replace_existing=True)
    scheduler.add_job(send_mailing,
                      'interval',
                      minutes=3,
                      id='send_mailing',
                      misfire_grace_time=30,
                      replace_existing=True,
                      max_instances=5,)
    return scheduler


class Command(BaseCommand):

    def handle(self, *args, **options):
        scheduler = scheduler_load('block')
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()

