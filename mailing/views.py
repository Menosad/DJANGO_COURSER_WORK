from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mailing.models import User


class MainListView(ListView):
    model = User
    template_name = 'mailing/index.html'


class MainDetailView(DetailView):
    model = User


