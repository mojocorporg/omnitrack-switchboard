from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel
from django.contrib.auth.models import User

# Create your models here.

class Transporter(TimeStampModel):
    """Fleet Owner Model"""

    def meta_default():
        return {"abc": "xyz"}

    transporter = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    company_address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15)
    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.transporter.username

    class Meta:
        verbose_name_plural = "Transporters"
