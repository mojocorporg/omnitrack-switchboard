from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel
from django.contrib.auth.models import User


# Create your models here.
JOB_STATUS_CHOICES = (
    (1, "Delay"),
    (2, "Loaded"),
    (3, "In Transit"),
)
RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10)
)


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

    operation_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="FO/CA"
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

    def __str__(self):
        self.commission_agent.username


FUEL_TYPE_CHOICE = (
    ("Deisel", "Deisel"),
    ("Petrol", "Petrol")
)


class VehicleType(TimeStampModel):
    """Model for Vehicle."""
    type = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)

    def __str__(self):
        return self.type + "(" + self.length + ", " + self.weight + ")"


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
    vehicle_type = models.ForeignKey(
        VehicleType, on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return self.registration_number


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

    def __str__(self):
        return self.vehicle.registration_number


class MaterialType(TimeStampModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


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
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE
    )
    material_to_carried = models.ForeignKey(
        MaterialType,
        on_delete=models.CASCADE,
        verbose_name="Material to be Carried"
    )
    weight = models.FloatField(verbose_name="Weight(kg)")


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
    price = models.FloatField()
    currency = models.ForeignKey(
        "common.Currency",
        on_delete=models.CASCADE
    )
    etd = models.PositiveSmallIntegerField(
        verbose_name="Estimated time of Delivery(Hrs)"
    )


class Job(TimeStampModel):
    """Job Models."""
    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE
    )
    delivery_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=JOB_STATUS_CHOICES)


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
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES
    )
    review = models.TextField()
