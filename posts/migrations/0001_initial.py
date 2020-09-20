# Generated by Django 3.1.1 on 2020-09-19 16:40

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sets.set')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
