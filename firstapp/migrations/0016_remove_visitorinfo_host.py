# Generated by Django 3.0.1 on 2019-12-31 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_visitorinfo_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorinfo',
            name='host',
        ),
    ]
