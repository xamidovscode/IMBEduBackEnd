from django.db import models

from apps.common.models import (
    BaseModel,

)
from apps.users.models import User

from helpers.choices import (
    GroupStatusChoices, AttendanceChoices, PaymentStatusChoices,
)


class GroupStudent(BaseModel):
    group = models.ForeignKey(
        'edu_platform.Group',
        related_name='group_students',
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        User,
        related_name='group_students',
        on_delete=models.CASCADE,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    payment_date = models.DateField()
    is_activated = models.BooleanField(
        default=False
    )
    status = models.IntegerField(
        choices=GroupStatusChoices.choices,
        default=GroupStatusChoices.ACTIVE,
    )


class Attendance(BaseModel):
    group_student = models.ForeignKey(
        GroupStudent,
        related_name='attendances',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    status = models.IntegerField(
        choices=AttendanceChoices.choices,
        default=AttendanceChoices.UNMARKED,
    )
    reason = models.TextField(
        null=True, blank=True,
    )


class GroupStudentDiscount(BaseModel):
    group_student = models.ForeignKey(
        GroupStudent,
        related_name='discounts',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        default=0,
    )
    count = models.IntegerField(
        default=1,
    )
    reason = models.TextField()
    author = models.ForeignKey(
        'users.User',
        related_name='discounts',
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        default=True,
    )


class GroupStudentPayment(BaseModel):
    group_student = models.ForeignKey(
        GroupStudent,
        related_name='payments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'users.User',
        related_name='payments',
        on_delete=models.CASCADE,
    )
    payment_type = models.ForeignKey(
        'common.PaymentType',
        related_name='payments',
        on_delete=models.CASCADE,
    )
    condition = models.IntegerField(
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PAYMENT,
    )
    amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        default=0,
    )
    description = models.TextField(
        null=True, blank=True,
    )
    date = models.DateField()





