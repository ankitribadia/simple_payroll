# Generated by Django 2.1.5 on 2019-02-08 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190208_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_at',
        ),
    ]
