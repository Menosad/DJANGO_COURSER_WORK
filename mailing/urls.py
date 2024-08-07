from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import add_mailing, MailingListView, CreateMailing

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='main'),
    path('add-mailing', add_mailing, name='add_mailing'),
    path('datetimepicker/', add_mailing, name='picker'),
]
