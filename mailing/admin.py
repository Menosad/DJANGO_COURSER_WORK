from django.contrib import admin

from mailing.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname')
    list_filter = ('nickname',)
