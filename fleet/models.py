from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel
from django.contrib.auth.models import User


# Create your models here.
class FleetOwner(TimeStampModel):
    """Fleet Owner Model"""

    def meta_default():
        return {"abc": "xyz"}

    fleet_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.fleet_owner.username

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
    chassis_number = models.CharField(max_length=255)
    engine_number = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=100, choices=FUEL_TYPE_CHOICE)
    color = models.CharField(max_length=255)
    meta = JSONField(default=meta_default)
    fleet_owner = models.ForeignKey(
        "FleetOwner",
        on_delete=models.CASCADE
    )


class VehicleType(TimeStampModel):
    """Model for Vehicle."""
    type = models.CharField(max_length=255)


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


class Lead(TimeStampModel):
    """Leads Model."""

    commission_agent = models.ForeignKey(
        "agent.CommissionAgent",
        on_delete=models.CASCADE
    )
    source = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="lead_source"
    )
    destination = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="lead_destination"
    )
    departure_date = models.DateField()
    vehicle = models.ForeignKey(
        "Vehicle",
        on_delete=models.CASCADE
    )
    material_to_carried = models.CharField(max_length=255)
    weight = models.CharField(max_length=20)


class Quote(TimeStampModel):
    """Quote Models"""
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE
    )
    commission_agent = models.ForeignKey(
        "agent.CommissionAgent",
        on_delete=models.CASCADE
    )
    vehicle = models.ForeignKey(
        "Vehicle",
        on_delete=models.CASCADE
    )
    price = models.CharField(max_length=100)
    etd = models.CharField(max_length=255, verbose_name="Estimated time of Delivery")


class Job(TimeStampModel):
    """Job Models."""
    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE
    )
    delivery_date = models.DateField()


class Rating(TimeStampModel):
    """Rating Models"""
    RATED_ENTITY_CHOICE = (
        (1, "Commission Agent"),
        (2, "Fleet Owner")
    )
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE
    )
    rated_entity = models.PositiveSmallIntegerField(
        choices=RATED_ENTITY_CHOICE
    )
    rating = models.CharField(max_length=50)
    review = models.TextField()
