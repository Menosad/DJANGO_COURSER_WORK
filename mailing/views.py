from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from mailing.models import User, Mailing



def index(request):
    return render(request, 'mailing/index.html')


def add_mailing(request, pk):
    user_name = User.objects.get(pk=pk).name
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        departure_date = request.POST.get('departure_date')
        at_work = request.POST.get('at_work')
        periodicity = request.POST.get('periodicity')

    return render(request, 'mailing/mailing_create.html')
