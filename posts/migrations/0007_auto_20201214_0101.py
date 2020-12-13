# Generated by Django 3.1.4 on 2020-12-13 19:01

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20201128_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=martor.models.MartorField(default=1),
            preserve_default=False,
        ),
    ]
