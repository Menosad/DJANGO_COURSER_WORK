from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import add_mailing, MailingListView, MailingDetailView, update_mailing, MailingDelete, \
    ClientCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='main'),
    path('mailing-detail/<int:pk>/', MailingDetailView.as_view(), name='detail'),
    path('mailing-edit/<int:pk>/', update_mailing, name='edit'),
    path('mailing-delete/<int:pk>/', MailingDelete.as_view(), name='delete'),
    path('add-mailing/', add_mailing, name='add_mailing'),
    path('add-client/', ClientCreateView.as_view(), name='add_client'),
]
