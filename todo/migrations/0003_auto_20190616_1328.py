# Generated by Django 2.2.1 on 2019-06-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190616_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
