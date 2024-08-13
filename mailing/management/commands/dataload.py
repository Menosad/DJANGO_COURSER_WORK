import json
import os
from django.core.management import BaseCommand
from mailing.models import Mailing
from users.models import User


path_collection = {
        "users": os.path.abspath('users.json'),
        'mailing': os.path.abspath('mailing.json')
}


def get_users_list():
    users_list = []
    with open(path_collection['users'], 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        for obj in json_file:
            user_dict = dict(pk=obj.get('pk'),
                             username=obj.get('fields').get('username'),
                             email=obj.get('fields').get('email'),
                             avatar=obj.get('fields').get('avatar'),
                             token=obj.get('fields').get('token'),
                             )
            users_list.append(User(**user_dict))
    return users_list


def get_mailing_list():
    mailing_list = []
    with open(path_collection['mailing'], 'r', encoding='utf-8') as file:
        json_dict = json.load(file)
        for obj in json_dict:
            user = User.objects.get(pk=obj.get('fields').get('user'))
            mailing_dict = dict(pk=obj.get('pk'),
                                title=obj.get('fields').get('title'),
                                content=obj.get('fields').get('content'),
                                departure_date=obj.get('fields').get('departure_date'),
                                at_work=obj.get('fields').get('at_work'),
                                periodicity=obj.get('fields').get('periodicity'),
                                user=user,
                                recipient_list=obj.get('fields').get('recipient_list'),
                                )
            mailing_list.append(Mailing(**mailing_dict))
    return mailing_list

class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        Mailing.objects.all().delete()
        users_list = get_users_list()
        User.objects.bulk_create(users_list)
        mailing_list = get_mailing_list()
        Mailing.objects.bulk_create(mailing_list)
        print('База данных обновлена успешно')
