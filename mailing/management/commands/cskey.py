import os

from django.core.management import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    def handle(self, *args, **options):
        key = get_random_secret_key()
        print(key)
