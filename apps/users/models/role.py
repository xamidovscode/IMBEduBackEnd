from apps.common.models import BaseModel
from django.db import models
from apps.users.models.user import User
from helpers import choices

class Role(models.Model):
    name = models.CharField(
        max_length=255,
    )
    is_active = models.BooleanField(
        default=True,
    )


# class Page(models.Model):
#     name = models.CharField(
#         max_length=255,
#         unique=True,
#     )
#     role = models.ForeignKey(
#         Role,
#         on_delete=models.CASCADE,
#         related_name="pages",
#     )
#
#
# class PageModule(models.Model):
#     pass
#
#
# class API(models.Model):
#     name = models.CharField(
#         max_length=255,
#         unique=True,
#     )
#     method = models.CharField(
#         max_length=255,
#         choices=choices.APIMethodChoices,
#         default=choices.APIMethodChoices.GET
#     )
#     dynamic = models.BooleanField(
#         default=False
#     )
#     page = models.ForeignKey(
#         Page,
#         on_delete=models.CASCADE,
#         related_name="api_pages",
#     )
#     role = models.ForeignKey(
#         Role,
#         on_delete=models.CASCADE,
#         related_name="apis",
#     )
#
