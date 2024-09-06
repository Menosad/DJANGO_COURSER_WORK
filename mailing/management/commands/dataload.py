import json
import os
from django.core.management import BaseCommand
from mailing.models import Mailing, Client
from users.models import User

path_collection = {
    "users": os.path.abspath('users.json'),
    'mailing': os.path.abspath('mailing.json'),
    'client': os.path.abspath('client_data.json')
}


def get_users_list():
    users_list = []
    with open(path_collection['users'], 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        for obj in json_file:
            user_dict = dict(pk=obj.get('pk'),
                             email=obj.get('fields').get('email'),
                             avatar=obj.get('fields').get('avatar'),
                             token=obj.get('fields').get('token'),
                             password=obj.get('fields').get('password'),
                             is_active=True if obj.get('fields').get('is_active') else False,
                             is_superuser=True if obj.get('fields').get('is_superuser') else False,
                             is_staff=True if obj.get('fields').get('is_staff') else False,
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


def get_client_list():
    client_list = []
    path_to_file = path_collection['client']
    with open(path_to_file, 'r') as file:
        readed_file = file.read()
        json_file = json.loads(readed_file)
        for client in json_file:
            user = User.objects.get(pk=client.get('fields').get('user'))
            client_dict = dict(name=client.get('fields').get('name'),
                               email=client.get('fields').get('email'),
                               user=user)
            client_list.append(Client(**client_dict))
    return client_list

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Mailing.objects.all().delete()
        Client.objects.all().delete()
        users_list = get_users_list()
        User.objects.bulk_create(users_list)
        mailing_list = get_mailing_list()
        Mailing.objects.bulk_create(mailing_list)
        client_list = get_client_list()
        Client.objects.bulk_create(client_list)
