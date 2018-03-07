from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel
from django.contrib.auth.models import User


# Create your models here.
class CommissionAgent(TimeStampModel):
    """Commssion Agent Model."""

    def meta_default():
        return {"abc": "xyz"}

    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    hub = models.CharField(max_length=15)
    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.agent.username

    class Meta:
        verbose_name_plural = "Commission Agents"
