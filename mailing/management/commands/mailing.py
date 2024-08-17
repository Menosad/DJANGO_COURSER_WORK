import logging
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mailing.models import Mailing

logger = logging.getLogger(__name__)


@util.close_old_connections
def delete_old_job_executions(max_age=86_400):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def scheduler_load():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(delete_old_job_executions, 'interval',
                      days=1, id='delete_old_job', replace_existing=True)
    mailing_list = Mailing.objects.filter(at_work=True)
    for i, mail in enumerate(mailing_list):
        timing = mail.periodicity + i
        scheduler.add_job(mail.send,
                          'interval',
                          minutes=timing,
                          id=mail.title,
                          misfire_grace_time=300,
                          replace_existing=True)
    return scheduler


class Command(BaseCommand):

    def handle(self, *args, **options):
        scheduler = scheduler_load()
        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
