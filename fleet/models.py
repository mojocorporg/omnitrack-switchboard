from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel

# Create your models here.
class FleetOwner(TimeStampModel):
    """Fleet Owner Model"""

    def meta_default():
        return {"abc": "xyz"}

    name = models.CharField(
        max_length=255,
        default=None
    )
    address = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    meta = JSONField(default=meta_default)

    class Meta:
        verbose_name_plural = "Fleet Owner List"


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


class Fleet(TimeStampModel):
    """Fleet Model."""

    def meta_default():
        return {"abc": "xyz"}

    truck_number = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    fleet_type = models.CharField(max_length=10)
    capacity = models.IntegerField()
    age = models.DateField(auto_now=False, auto_now_add=False)
    meta = JSONField(default=meta_default)
    fleet_owner = models.ForeignKey(
        "FleetOwner",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Fleet List"


class Operation(TimeStampModel):
    """Operation Model."""

    commission_agent = models.ForeignKey(
        "CommissionAgent",
        on_delete=models.CASCADE
    )
    fleet_owner = models.ForeignKey(
        "FleetOwner",
        on_delete=models.CASCADE
    )
    source = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="source"
    )
    destination = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="destination"
    )

    class Meta:
        verbose_name_plural = "Operation List"


class Feed(TimeStampModel):
    """Feed Model."""

    vehicle = models.ForeignKey(
        "common.Vehicle",
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Feed List"
