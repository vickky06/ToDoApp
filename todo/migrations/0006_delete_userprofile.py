# Generated by Django 2.2.1 on 2019-06-19 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
