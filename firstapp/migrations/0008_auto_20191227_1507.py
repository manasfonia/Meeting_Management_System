# Generated by Django 3.0.1 on 2019-12-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20191220_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitorinfo',
            old_name='email_id',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='visitorinfo',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
