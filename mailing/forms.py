from django import forms

from mailing.models import Client


class ClientMailingForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('user',)
