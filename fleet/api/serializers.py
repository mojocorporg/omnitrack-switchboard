from rest_framework import serializers
from fleet.models import (
    FleetOwner, Operation, Feed, Vehicle, VehicleType,
    Lead, Rating, Job, Quote, MaterialType
)


class FleetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetOwner
        fields = ("id", "fleet_owner", "address", "phone", "meta")


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = (
            "id", "operation_user", "source", "destination"
        )


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "vehicle", "city")


class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = ("id", "name")


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id", "name", "brand", "model", "model_number", "registration_number",
            "chassis_number", "engine_number", "body_type", "fuel_type", "color",
            "meta", "fleet_owner",
        )


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = (
            "id", "type", "length", "weight"
        )


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "id", "commission_agent", "source", "destination",
            "departure_date", "vehicle_type", "material_to_carried",
            "weight"
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            "id", "lead", "commission_agent", "vehicle",
            "price", "etd"
        )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "id", "quote", "delivery_date", "status"
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            "id", "job", "rated_entity", "rating", "review"
        )
