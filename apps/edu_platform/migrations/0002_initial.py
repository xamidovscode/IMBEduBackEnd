# Generated by Django 5.2.2 on 2025-06-19 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('edu_platform', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grouplessonday',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_of_weeks', to='edu_platform.group'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_students', to='edu_platform.group'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendance',
            name='group_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='edu_platform.groupstudent'),
        ),
        migrations.AddField(
            model_name='groupstudentdiscount',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupstudentdiscount',
            name='group_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='edu_platform.groupstudent'),
        ),
        migrations.AddField(
            model_name='groupstudentpayment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupstudentpayment',
            name='group_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='edu_platform.groupstudent'),
        ),
        migrations.AddField(
            model_name='groupstudentpayment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='common.paymenttype'),
        ),
    ]
