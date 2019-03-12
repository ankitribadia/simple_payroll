# Generated by Django 2.1.5 on 2019-03-08 06:08

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('Designation', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('full_name', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField(default=0)),
                ('dob', models.DateField(blank=True)),
                ('date_joined', models.DateField(blank=True)),
                ('salary', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=9)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_start', models.CharField(max_length=5)),
                ('time_end', models.CharField(max_length=5)),
                ('shift_duration', models.CharField(max_length=5)),
                ('shift_month_duration', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Shift'),
        ),
    ]
