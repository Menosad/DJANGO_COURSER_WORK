
from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    # def ready(self):
    #     from mailing.management.commands.mailing import scheduler_load
    #     scheduler = scheduler_load('back')
    #     from time import sleep
    #     sleep(1)
    #     scheduler.start()
