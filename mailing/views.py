import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from mailing.models import Mailing, MailingAttempt, Client


class MailingListView(LoginRequiredMixin, ListView):
    extra_context = {'title': 'список рассылок'}
    model = Mailing
    template_name = 'mailing/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        client_list = Client.objects.filter(user=self.request.user.pk)
        context['client_list'] = client_list
        return context

    def get_queryset(self):
        list_object = super().get_queryset()
        user_pk = self.request.user.pk
        new_list = list_object.filter(user=user_pk)
        for mail in new_list:
            mail.attempts = len(MailingAttempt.objects.filter(mailing__pk=mail.pk).filter(status=True))
        return new_list


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
        start_date = request.POST.get('departure_date').replace('/', '-', 3)
        obj.departure_date = datetime.datetime.fromisoformat(start_date + '+03:00')
        obj.at_work = request.POST.get('at_work')
        obj.periodicity = request.POST.get('periodicity')
        obj.recipient_list = request.POST.get('recipient_list')
        obj.save()
        return redirect(f'/mailing-detail/{pk}/')
    return render(request, 'mailing/mailing_update.html', {'obj': obj, })


def add_mailing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        start_date = request.POST.get('departure_date').replace('/', '-', 3)
        departure_date = datetime.datetime.fromisoformat(start_date + '+03:00')
        periodicity = request.POST.get('periodicity')
        recipient_list = request.POST.get('recipient_list')
        mailing = Mailing.objects.create(title=title, content=content, departure_date=departure_date,
                                         periodicity=periodicity,
                                         user=request.user,
                                         recipient_list=recipient_list
                                         )
        mailing.save()
        request.path = f'mailing-detail/{mailing.pk}'
        return redirect(to=request.path)
    return render(request, 'mailing/mailing_create.html')


class ClientDetail(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email')

    def form_valid(self, form):
        object = form.save()
        if form.is_valid():
            object.user = self.request.user.pk
            object.save()
        return super().form_valid(form)
