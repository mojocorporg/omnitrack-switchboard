from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    """Abstract Base Class Model for created_at and last_updated
     at Datetime Fields"""

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(TimeStampModel):
    """Model for Country."""

    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class State(TimeStampModel):
    """Model for States."""

    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class City(TimeStampModel):
    """Model for City."""

    name = models.CharField(max_length=200)
    state = models.ForeignKey(
        "State",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


FUEL_TYPE_CHOICE = (
    ("Deisel", "Deisel"),
    ("Petrol", "Petrol")
)


class Vehicle(TimeStampModel):
    """Model for Vehicle."""

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
