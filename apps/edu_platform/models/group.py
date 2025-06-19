from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User

from helpers.choices import (
    GroupStatusChoices,
    DayOfWeekChoices,
)


class Group(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.IntegerField(
        choices=GroupStatusChoices.choices,
        default=GroupStatusChoices.ACTIVE,
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='edu_groups',
    )
    course = models.ForeignKey(
        'common.Course',
        on_delete=models.CASCADE,
        related_name='groups',
    )
    room = models.ForeignKey(
        'common.Room',
        on_delete=models.CASCADE,
        related_name='groups',
    )
    branch = models.ForeignKey(
        'common.Branch',
        on_delete=models.CASCADE,
        related_name='groups',
    )


class GroupLessonDay(BaseModel):
    group = models.ForeignKey(
        Group,
        related_name='day_of_weeks',
        on_delete=models.CASCADE,
    )
    day_of_week = models.IntegerField(
        choices=DayOfWeekChoices.choices,
        default=DayOfWeekChoices.MONDAY,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(
        default=True,
    )






