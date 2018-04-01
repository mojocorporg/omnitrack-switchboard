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
    filter_fields = ("commission_agent",)

    def get_serializer_class(self):
        if self.action == 'list':
            return LeadListSerializer
        elif self.action == 'retrieve':
            return LeadListSerializer
        return LeadSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    filter_fields = ("lead", "commission_agent")

    def get_serializer_class(self):
        if self.action == 'list':
            return QuoteListSerializer
        return QuoteSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    filter_fields = ("quote", "quote__commission_agent", "quote__lead")

    def get_serializer_class(self):
        if self.action == 'list':
            return JobListSerializer
        return JobSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
