# Generated by Django 3.0.5 on 2020-05-17 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_urlshort_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshort',
            name='no',
        ),
    ]
