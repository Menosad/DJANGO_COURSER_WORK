from django.contrib.auth.views import LoginView
from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('user-login/', LoginView.as_view(template_name=''), name='login'),

]
