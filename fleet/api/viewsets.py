from rest_framework.response import Response
from rest_framework import viewsets
from fleet.models import *
from .serializers import (
    FleetOwnerSerializer, OperationSerializer,
    FeedSerializer, VehicleSerializer, VehicleTypeSerializer,
    LeadSerializer, QuoteSerializer, JobSerializer, RatingSerializer,
    MaterialTypeSerializer, LeadListSerializer, OperationListSerializer,
    FeedListSerializer, QuoteListSerializer, JobListSerializer
)


class FleetOwnerViewSet(viewsets.ModelViewSet):
    queryset = FleetOwner.objects.all()
    serializer_class = FleetOwnerSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OperationListSerializer
        return OperationSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return FeedListSerializer
        return FeedSerializer


class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return LeadListSerializer
        elif self.action == 'retrieve':
            return LeadListSerializer
        return LeadSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        lead_id = self.request.query_params.get('lead_id', None)
        commissionagent_id = self.request.query_params.get('commissionagent_id', None)
        if lead_id is not None:
            return queryset.filter(lead__id=lead_id)
        if commissionagent_id is not None:
            return queryset.filter(commission_agent__id=commissionagent_id)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return QuoteListSerializer
        return QuoteSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return JobListSerializer
        return JobSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
