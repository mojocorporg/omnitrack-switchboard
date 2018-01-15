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
        verbose_name_plural = "Fleet Owners"


class Operation(TimeStampModel):
    """Operation Model."""

    commission_agent = models.ForeignKey(
        "agent.CommissionAgent",
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
        verbose_name_plural = "Operations"


FUEL_TYPE_CHOICE = (
    ("Deisel", "Deisel"),
    ("Petrol", "Petrol")
)


class Vehicle(TimeStampModel):
    """Model for Vehicle."""

    def meta_default():
        return {"abc": "xyz"}

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    chasis_number = models.CharField(max_length=255)
    engine_number = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=100, choices=FUEL_TYPE_CHOICE)
    color = models.CharField(max_length=255)
    meta = JSONField(default=meta_default)
    fleet_owner = models.ForeignKey(
        "FleetOwner",
        on_delete=models.CASCADE
    )


class Feed(TimeStampModel):
    """Feed Model."""

    vehicle = models.ForeignKey(
        "Vehicle",
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Feeds"
