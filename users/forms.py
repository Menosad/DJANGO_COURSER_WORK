from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import BooleanField

from users.models import User


class ValidationFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(ValidationFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserEditForm(ValidationFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
