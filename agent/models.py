from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel, State
from django.contrib.auth.models import User


# Create your models here.
class CommissionAgent(TimeStampModel):
    """Commssion Agent Model."""

    def meta_default():
        return {"abc": "xyz"}

    profile_pic = models.ImageField(null=True, blank=True)
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    company_address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15)
    hub = models.ManyToManyField(State, db_index=True, blank=True)
    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.agent.username

    class Meta:
        verbose_name_plural = "Commission Agents"
