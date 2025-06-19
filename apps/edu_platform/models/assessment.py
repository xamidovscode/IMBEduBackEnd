from django.db import models

from apps.common.models import BaseModel
from helpers.choices import PaymentStatusChoices, AssessmentSubmissionChoices


class Assessment(BaseModel):
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='assessments',
    )
    group = models.ForeignKey(
        'edu_platform.Group',
        on_delete=models.CASCADE,
        related_name='assessments',
    )
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        null=True, blank=True,
    )
    date = models.DateField()
    deadline = models.DateTimeField()
    type = models.IntegerField(
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PAYMENT,
    )


class AssessmentSubmissions(BaseModel):
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name='submissions',
    )
    group_student = models.ForeignKey(
        'edu_platform.GroupStudent',
        on_delete=models.CASCADE,
        related_name='submissions',
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    status = models.IntegerField(
        choices=AssessmentSubmissionChoices.choices,
        default=AssessmentSubmissionChoices.NEW,
    )
    reason = models.TextField(
        null=True, blank=True,
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='submissions',
    )


