from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.get(username='admin'):
            User.objects.get(username='admin').delete()
            admin = User.objects.create(
                username='admin',
                email='admin@email.com',
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
            admin.set_password('admin')
            admin.save()
