from django.db import models


class APIMethodChoices(models.IntegerChoices):
    GET = 1, 'GET'
    POST = 2, 'POST'
    PUT = 3, 'PUT'
    PATCH = 4, 'PATCH'
    DELETE = 5, 'DELETE'


class GroupStatusChoices(models.IntegerChoices):
    ACTIVE = 1, 'ACTIVE'
    NEW = 2, 'NEW'
    DELETED = 3, 'DELETED'
    FROZEN = 4, 'FROZEN'


class DayOfWeekChoices(models.IntegerChoices):
    MONDAY = 1, 'MONDAY'
    TUESDAY = 2, 'TUESDAY'
    THURSDAY = 3, 'THURSDAY'
    FRIDAY = 4, 'FRIDAY'
    SATURDAY = 5, 'SATURDAY'
    SUNDAY = 6, 'SUNDAY'
    WEDNESDAY = 7, 'WEDNESDAY'


class AttendanceChoices(models.IntegerChoices):
    ABSENT = -1, 'Absent'
    UNMARKED = 0, 'Unmarked'
    PRESENT = 1, 'Present'
    EXCUSED = 2, 'Excused'


class PaymentStatusChoices(models.IntegerChoices):
    PAYMENT = 1, 'Payment'
    DEBT = 2, 'Debt'


class AssessmentSubmissionChoices(models.IntegerChoices):
    NEW = 1, 'New'
    SENT = 2, 'Sent'
    SCORED = 3, 'Scored'


