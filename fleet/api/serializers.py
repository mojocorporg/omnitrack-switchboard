from rest_framework import serializers
from fleet.models import (
    FleetOwner, Operation, Feed, Vehicle
)


class FleetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetOwner
        fields = ("id", "name", "address", "email", "phone", "meta")


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = (
            "id", "commission_agent", "fleet_owner", "source", "destination"
        )


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "vehicle", "city")


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id", "name", "brand", "model", "model_number", "registration_number"
            "chasis_number", "engine_number", "body_type", "fuel_type", "color",
            "meta", "fleet_owner",
        )
