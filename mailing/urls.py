from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import UserListView, UserDetailView, UserCreateView, UserDeleteView, \
    UserUpdateView, add_mailing

app_name = MailingConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('create_mailing/', add_mailing, name='create_mailing'),
]
