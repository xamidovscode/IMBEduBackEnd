from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class Branch(BaseModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Role(BaseModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)



