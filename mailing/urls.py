from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import add_mailing, index

app_name = MailingConfig.name

urlpatterns = [
    path('', index, name='main'),
    path('add_mailing/<int:pk>', add_mailing, name='add_mailing'),
]
