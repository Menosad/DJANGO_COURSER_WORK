# Generated by Django 5.1 on 2024-08-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0016_alter_mailing_recipient_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='recipient_list',
            field=models.TextField(blank=True, null=True, verbose_name='список получателей'),
        ),
    ]