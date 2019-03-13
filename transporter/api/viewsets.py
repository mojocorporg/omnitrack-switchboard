from rest_framework.response import Response
from rest_framework import viewsets
from transporter.models import *
from .serializers import TransporterSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class TransporterViewSet(viewsets.ModelViewSet):
    queryset = Transporter.objects.all()
    serializer_class = TransporterSerializer

