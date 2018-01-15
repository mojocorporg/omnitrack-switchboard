from rest_framework.response import Response
from rest_framework import viewsets
from fleet.models import FleetOwner, CommissionAgent, Operation, Feed, Vehicle
from .serializers import (
    FleetOwnerSerializer, CommissionAgentSerializer, OperationSerializer,
    FeedSerializer, VehicleSerializer
)


class FleetOwnerViewSet(viewsets.ModelViewSet):
    queryset = FleetOwner.objects.all()
    serializer_class = FleetOwnerSerializer


class CommissionAgentViewSet(viewsets.ModelViewSet):
    queryset = CommissionAgent.objects.all()
    serializer_class = CommissionAgentSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
