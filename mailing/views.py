from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from mailing.models import User, Mailing


class MailingListView(ListView):
    extra_context = {'title': 'список рассылок'}
    model = Mailing
    template_name = 'mailing/index.html'


class CreateMailing(CreateView):
    extra_context = {'title': 'список рассылок'}
    model = Mailing
    success_url = reverse_lazy('mailing:index.html')


def add_mailing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        departure_date = request.POST.get('departure_date').replace('/', '-', 3)
        at_work = request.POST.get('at_work')
        periodicity = request.POST.get('periodicity')
        user = request.user
        print(f'departure_date={departure_date, type(departure_date)}, periodicity={periodicity, type(periodicity)}')
        mailing = Mailing.objects.create(title=title, content=content, departure_date=departure_date,
                                         at_work=at_work,
                                         periodicity=periodicity,
                                         user=request.user)
        mailing.save()
    return render(request, 'mailing/mailing_create.html')
