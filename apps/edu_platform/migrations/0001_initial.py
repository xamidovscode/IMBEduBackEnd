# Generated by Django 5.2.2 on 2025-06-19 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(-1, 'Absent'), (0, 'Unmarked'), (1, 'Present'), (2, 'Excused')], default=0)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupLessonDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day_of_week', models.IntegerField(choices=[(1, 'MONDAY'), (2, 'TUESDAY'), (3, 'THURSDAY'), (4, 'FRIDAY'), (5, 'SATURDAY'), (6, 'SUNDAY'), (7, 'WEDNESDAY')], default=1)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('payment_date', models.DateField()),
                ('is_activated', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'NEW'), (3, 'DELETED'), (4, 'FROZEN')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupStudentDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('count', models.IntegerField(default=1)),
                ('reason', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupStudentPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('condition', models.IntegerField(choices=[(1, 'Payment'), (2, 'Debt')], default=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'NEW'), (3, 'DELETED'), (4, 'FROZEN')], default=1)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='common.branch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='common.course')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='common.room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
