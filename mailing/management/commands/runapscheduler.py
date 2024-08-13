import datetime
import logging
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mailing.models import Mailing

logger = logging.getLogger(__name__)
mailing_list = Mailing.objects.all()


def generate_job():
    """Функция генерирующая функции для выполнения рассылок"""
    pass

def start_mailing():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(delete_old_job_executions, 'interval',
                      days=1, id='delete_old_job', replace_existing=True)
    scheduler.add_job()
    scheduler.start()


@util.close_old_connections
def delete_old_job_executions(max_age=60):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        pass
