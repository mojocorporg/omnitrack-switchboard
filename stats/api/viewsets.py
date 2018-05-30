from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


class UserIncreasedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for retrieving users.
    """
    def retrieve(self, request):
        total_users = User.objects.all().count()
        users_increased = User.objects.all().filter(date_joined__gte=(timezone.now() - timedelta(days=7))).count()
        return Response(
            {
                "total": total_users,
                "last_week": users_increased
            }
        )

class TonnageIncreasedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving tonnage.
    """
    def retrieve(self, request):
        return Response(
            {
                "total": 0,
                "last_week": 0
            }
        )

class LeadIncreasedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving leads.
    """
    def retrieve(self, request):
        return Response(
            {
                "total": 0,
                "last_week": 0
            }
        )


class TopDestinationViewSet(viewsets.ViewSet):
    """
    Get a simple stats for top destination having max number of leads
    """
    def list(self, request):
        return Response([
            {
                "id": 0,
                "city": "Test",
                "leads": 123,
                "tonnage": 63821
            }
        ])


class TopSourceViewSet(viewsets.ViewSet):
    """
    Get a simple stats for top origin points having max number of leads
    """
    def list(self, request):
        return Response([
            {
                "id": 0,
                "city": "Test",
                "leads": 123,
                "tonnage": 63821
            }
        ])
