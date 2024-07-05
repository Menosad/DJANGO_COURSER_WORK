from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MainListView, MainDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('', MainListView.as_view()),
    path('user_detail/<int:pk>', MainDetailView.as_view(), name='user_detail'),
]
