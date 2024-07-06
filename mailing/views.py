from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mailing.models import User, Mailing


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('title', 'content', 'departure_date', 'periodicity')
    success_url = reverse_lazy('mailing:user_list.html')
