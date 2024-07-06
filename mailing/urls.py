from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import UserListView, UserDetailView, MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
]
