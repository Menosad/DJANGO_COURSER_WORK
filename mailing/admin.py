from django.contrib import admin
from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'departure_date', 'at_work', 'periodicity',)
    list_filter = ('title', 'user',)
    search_fields = ('title', 'departure_date',)
