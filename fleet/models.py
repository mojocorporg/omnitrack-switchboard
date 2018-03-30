from django.contrib.postgres.fields import JSONField
from django.db import models
from common.models import TimeStampModel
from django.contrib.auth.models import User


# Create your models here.
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

    fleet_owner = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
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
        verbose_name="FO/CA", db_index=True
    )
    source = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="source", db_index=True
    )
    destination = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="destination", db_index=True
    )

    class Meta:
        verbose_name_plural = "Operations"


FUEL_TYPE_CHOICE = (
    ("Deisel", "Deisel"),
    ("Petrol", "Petrol")
)


class VehicleType(TimeStampModel):
    """Model for Vehicle."""

    def meta_default():
        return {"abc": "xyz"}

    type = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.type + "(" + self.length + ", " + self.weight + ")"


class Vehicle(TimeStampModel):
    """Model for Vehicle."""

    def meta_default():
        return {"abc": "xyz"}

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    model_number = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(max_length=255, db_index=True, unique=True)
    chassis_number = models.CharField(max_length=255, null=True, blank=True)
    engine_number = models.CharField(max_length=255, null=True, blank=True)
    body_type = models.CharField(max_length=255, null=True, blank=True)
    fuel_type = models.CharField(max_length=100, choices=FUEL_TYPE_CHOICE)
    color = models.CharField(max_length=255, null=True, blank=True)
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
        on_delete=models.CASCADE, db_index=True
    )
    city = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE, db_index=True
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
    title = models.CharField(max_length=200, null=True, blank=True)
    commission_agent = models.ForeignKey(
        "agent.CommissionAgent",
        on_delete=models.CASCADE, db_index=True
    )
    source = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="lead_source", db_index=True
    )
    destination = models.ForeignKey(
        "common.City",
        on_delete=models.CASCADE,
        related_name="lead_destination", db_index=True
    )
    departure_date = models.DateField()
    departure_time = models.TimeField(blank=True, null=True)
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE, db_index=True
    )
    material_to_carried = models.ForeignKey(
        MaterialType,
        on_delete=models.CASCADE,
        verbose_name="Material to be Carried", db_index=True
    )
    weight = models.FloatField(verbose_name="Weight(kg)")

    def __str__(self):
        self.title


class Quote(TimeStampModel):
    """Quote Models"""
    title = models.CharField(max_length=200, null=True, blank=True)
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE
    )
    commission_agent = models.ForeignKey(
        "agent.CommissionAgent",
        on_delete=models.CASCADE, db_index=True
    )
    vehicle = models.ForeignKey(
        "Vehicle",
        on_delete=models.CASCADE,
        null=True, blank=True, db_index=True
    )
    price = models.FloatField()
    currency = models.ForeignKey(
        "common.Currency",
        on_delete=models.CASCADE, db_index=True
    )
    etd = models.PositiveSmallIntegerField(
        verbose_name="Estimated time of Delivery(Hrs)", db_index=True
    )

    def __str__(self):
        self.title


class JobStatus(TimeStampModel):
    """Job Models."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Job(TimeStampModel):
    """Job Models."""
    title = models.CharField(max_length=200, null=True, blank=True)
    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE, db_index=True
    )
    delivery_date = models.DateField()
    status = models.ForeignKey(
        JobStatus, on_delete=models.CASCADE, db_index=True
    )

    def __str__(self):
        self.title


class Rating(TimeStampModel):
    """Rating Models"""
    RATED_ENTITY_CHOICE = (
        (1, "Commission Agent"),
        (2, "Fleet Owner")
    )
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, db_index=True
    )
    rated_entity = models.PositiveSmallIntegerField(
        choices=RATED_ENTITY_CHOICE, db_index=True
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, db_index=True
    )
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job.title + " got " + self.rating
