from rest_framework import serializers
from fleet.models import (
    FleetOwner, Operation, Feed, Vehicle, VehicleType,
    Lead, Rating, Job, Quote, MaterialType
)


class FleetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetOwner
        fields = (
            "id", "fleet_owner", "company_name", "company_address", "phone", "meta"
        )


class OperationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
        depth = 1


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ("id", "operation_user", "source", "destination")


class FeedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1


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
        fields = "__all__"


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = (
            "id", "type", "length", "weight", "meta"
        )


class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"
        depth = 1


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "id" ,"transporter", "commission_agent", "departure_time", "departure_date",
            "source", "destination", "vehicle_type", "material_to_carried", "weight"
        )


class QuoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"
        depth = 1


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("id", "lead", "commission_agent", "vehicle", "price",
        "currency", "etd", "fleet_owner")


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        depth = 3


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "quote", "delivery_date", "status")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
