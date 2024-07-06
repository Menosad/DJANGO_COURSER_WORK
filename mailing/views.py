from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from mailing.models import User, Mailing


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = ('name', 'nickname', 'label')
    success_url = reverse_lazy('mailing:user_list')


class UserUpdateView(UpdateView):
    model = User
    fields = ('name', 'nickname', 'label')
    success_url = reverse_lazy('mailing:user_list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('mailing:user_list')


def add_mailing(request):

    return render(request, 'mailing/mailing_form.html')
