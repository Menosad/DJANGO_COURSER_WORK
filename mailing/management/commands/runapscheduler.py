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
start = datetime.datetime.now() + datetime.timedelta(seconds=5)
end = datetime.datetime.now() + datetime.timedelta(seconds=15)


mailing_list = Mailing.objects.all()

word_list = ['1testsss', '1new world', 'grace for me']
job_list = []
for word in word_list:
    def job():
        print(word)

    job_list.append(job)


@util.close_old_connections
def delete_old_job_executions(max_age=60):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        for i, job in enumerate(job_list):
            scheduler.add_job(
                job,
                'interval',
                seconds=i+5,
                id=word_list[i],
                replace_existing=True,
                max_instances=1,
                misfire_grace_time=5,
            )
            logger.info('Работа добавлена')
        scheduler.start()
