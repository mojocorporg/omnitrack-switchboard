from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel


# Create your models here.
class CommissionAgent(TimeStampModel):
    """Commssion Agent Model."""

    def meta_default():
        return {"abc": "xyz"}

    name = models.CharField(
        max_length=255,
        default=None
    )
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    hub = models.CharField(max_length=15)
    meta = JSONField(default=meta_default)

    class Meta:
        verbose_name_plural = "Commission Agents"
