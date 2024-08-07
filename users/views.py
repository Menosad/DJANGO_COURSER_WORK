import os
import secrets

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            token = secrets.token_hex(16)
            user.token = token
            user.is_active = False
            user.save()
            host = self.request.get_host()
            url = f'http://{host}/users/email-confirm/{token}/'
            send_mail(
                subject='Подтверждение регистрации',
                message=f"Вы прошли регистрацию на сайте управления рассылками mailing для завершения регистрации пожалуйста пройдите по ссылке:\n"
                         f"{url}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
                auth_user=None,
                auth_password=None,
                connection=None,
                html_message=None,
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verify', args=(self.object.id,))


class UserProfileView(DetailView):
    model = User


def verify_user(request, pk):
    user = User.objects.get(pk=pk)
    email = user.email
    index = email.find('@') + 1
    email_provider = 'https://' + email[index:]
    context = {'email_provider': email_provider}
    return render(request, 'users/verify.html', context)


def email_confirm(request, token):
    user = User.objects.get(token=token)
    user.is_active = True
    user.save()
    context = {'username': user.username}
    return render(request, 'users/validation.html', context)


