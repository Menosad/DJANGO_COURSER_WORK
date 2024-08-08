from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from mailing.models import User, Mailing


def edit_mailing(request, *args, **kwargs):
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
        return mailing


class MailingListView(ListView):
    extra_context = {'title': 'список рассылок'}
    model = Mailing
    template_name = 'mailing/index.html'

    def get_queryset(self):
        list_object = super().get_queryset()
        if isinstance(self.request.user, int):
            new_list = list_object.filter(user=self.request.user)
            return new_list
        else:
            return list_object


class MailingDetailView(DetailView):
    model = Mailing


class MailingDelete(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:main')


def update_mailing(request, pk):
    obj = Mailing.objects.get(pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.content = request.POST.get('content')
        obj.departure_date = request.POST.get('departure_date').replace('/', '-', 3)
        obj.at_work = request.POST.get('at_work')
        obj.periodicity = request.POST.get('periodicity')
        obj.save()
        request.path = f'mailing-detail/{obj.pk}'
        return redirect(to=f'/')
    return render(request, 'mailing/mailing_create.html')


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
