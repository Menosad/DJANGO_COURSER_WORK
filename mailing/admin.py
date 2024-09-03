from django.contrib import admin
from mailing.models import Mailing, MailingAttempt, Client


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'departure_date', 'at_work',)
    list_filter = ('title', 'user',)
    search_fields = ('title', 'departure_date',)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing', 'status', 'server_response', 'last_try', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
