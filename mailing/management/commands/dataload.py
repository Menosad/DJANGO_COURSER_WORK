import json
import os
from django.core.management import BaseCommand
from mailing.models import Mailing
from users.models import User


class Command(BaseCommand):
    path_list = [
        os.path.abspath('users.json'),
        os.path.abspath('mailing.json')
    ]

    def handle(self, *args, **options):
        mailing_list = Mailing.objects.all()
        users_list = User.objects.all()
        result_tuple = ([], [])
        for i, path in enumerate(Command.path_list):
            with open(path, 'r', encoding='utf-8') as file:
                json_file = json.load(file)
                for obj in json_file:
                    if obj.get('model') == 'users.user':
                        user_dict = dict(username=obj.get('fields').get('username'),
                                         email=obj.get('fields').get('email'),
                                         avatar=obj.get('fields').get('avatar'),
                                         is_superuser=obj.get('fields').get('is_superuser'),
                                         first_name=obj.get('fields').get('first_name'),
                                         is_staff=obj.get('fields').get('is_staff'),
                                         is_active=obj.get('fields').get('is_active'),
                                         date_joined=obj.get('fields').get('date_joined'),
                                         token=obj.get('fields').get('token'),
                                         groups=obj.get('fields').get('groups'),
                                         user_permissions=obj.get('fields').get('user_permissions'),
                                         pk=obj.get('pk'))

                        result_tuple[i].append(User(**user_dict))
                    elif obj.get('model') == 'mailing.mailing':
                        mailing_dict = dict(pk=obj.get('pk'),
                                            title=obj.get('fields').get('title'),
                                            content=obj.get('fields').get('content'),
                                            departure_date=obj.get('fields').get('departure_date'),
                                            at_work=obj.get('fields').get('at_work'),
                                            periodicity=obj.get('fields').get('periodicity'),
                                            user=obj.get('fields').get('user'),
                                            )
                        result_tuple[i].append(Mailing(**user_dict))
                    print(User.__class__.__name__, Mailing.__class__.__name__)
                    #User.objects.bulk_create(result_tuple[0])
