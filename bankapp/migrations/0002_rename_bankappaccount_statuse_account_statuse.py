# Generated by Django 5.1 on 2024-09-02 11:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BankappAccount_Statuse',
            new_name='Account_Statuse',
        ),
    ]
