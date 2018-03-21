from django.db import models
from django.contrib.postgres.fields import JSONField


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
    code = models.CharField(max_length=2, unique=True, db_index=True)
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
    code = models.CharField(max_length=2, unique=True, db_index=True)
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


class Currency(TimeStampModel):
    """Model for Currency."""

    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + "(" + self.symbol + ")"

    class Meta:
        verbose_name_plural = "Currencies"
