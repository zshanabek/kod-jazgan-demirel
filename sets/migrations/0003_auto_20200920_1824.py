# Generated by Django 3.1.1 on 2020-09-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sets', '0002_auto_20200920_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='cover',
            field=models.ImageField(height_field=100, null=True, upload_to='sets', verbose_name='Cover', width_field=100),
        ),
    ]
