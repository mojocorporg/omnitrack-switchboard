from rest_framework import generics
from django_filters import rest_framework as filters
from fleet.models import Lead


class LeadFilter(filters.FilterSet):
    gte_created_at = filters.DateTimeFilter(name="created_at", lookup_expr="gte")
    gte_departure_date = filters.DateFilter(name="departure_date", lookup_expr="gte")

    class Meta:
        model = Lead
        fields = [
            "gte_created_at", "gte_departure_date", "commission_agent", "source",
            "destination", "vehicle_type", "transporter"
        ]
