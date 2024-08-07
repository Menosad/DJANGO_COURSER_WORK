from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegisterView, verify_user, email_confirm, UserProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('user-login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('user-logout/', LogoutView.as_view(), name='logout'),
    path('user-register/', UserRegisterView.as_view(), name='register'),
    path('user-profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('user-verify/<int:pk>', verify_user, name='verify'),
    path('email-confirm/<str:token>/', email_confirm, name='confirm'),

]
