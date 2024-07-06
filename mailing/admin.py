from django.contrib import admin

from mailing.models import User, Mailing


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname')
    list_filter = ('nickname',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'departure_date', 'at_work', 'periodicity',)
    list_filter = ('title', 'user',)
    search_fields = ('title', 'departure_date',)
