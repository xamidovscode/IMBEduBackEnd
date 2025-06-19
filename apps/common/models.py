from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class Branch(BaseModel):
    name = models.CharField(
        max_length=100
    )
    is_active = models.BooleanField(
        default=True
    )


class Room(BaseModel):
    name = models.CharField(
        max_length=100
    )
    branch = models.ForeignKey(
        Branch,
        related_name='rooms',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        default=True
    )


class Course(BaseModel):
    name = models.CharField(
        max_length=100
    )
    branch = models.ForeignKey(
        Branch,
        related_name='courses',
        on_delete=models.PROTECT,
    )
    price = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        default=0,
    )
    duration = models.PositiveIntegerField(
        default=0,
    )
    is_active = models.BooleanField(
        default=True
    )
    color = models.CharField(
        max_length=100,
        null=True, blank=True,
    )


class Source(BaseModel):
    name = models.CharField(
        max_length=100,
    )
    icon = models.CharField(
        max_length=100,
        null=True, blank=True,
    )
    is_active = models.BooleanField(
        default=True
    )


class PaymentType(BaseModel):
    name = models.CharField(
        max_length=100
    )
    is_active = models.BooleanField(
        default=True
    )

class Setting(BaseModel):
    name = models.CharField(
        max_length=100
    )
    open_time = models.TimeField()
    close_time = models.TimeField()
    logo = models.ImageField(
        null=True, blank=True,
    )
    extra_data = models.JSONField(
        default=dict,
    )







