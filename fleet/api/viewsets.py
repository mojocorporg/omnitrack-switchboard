from rest_framework.response import Response
from rest_framework import viewsets
from fleet.models import *
from .serializers import (
    FleetOwnerSerializer, OperationSerializer,
    FeedSerializer, VehicleSerializer, VehicleTypeSerializer,
    LeadSerializer, QuoteSerializer, JobSerializer, RatingSerializer
)


class FleetOwnerViewSet(viewsets.ModelViewSet):
    queryset = FleetOwner.objects.all()
    serializer_class = FleetOwnerSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
