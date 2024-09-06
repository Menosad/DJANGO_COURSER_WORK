from django.core.management import BaseCommand
from django_apscheduler.models import DjangoJobExecution, DjangoJob


class Command(BaseCommand):
    def handle(self, *args, **options):
        DjangoJobExecution.objects.delete_old_job_executions(max_age=10)
        DjangoJob.objects.all().delete()
