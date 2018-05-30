from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone

class UserIncreasedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def retrieve(self, request):
        total_users = User.objects.all().count()
        users_increased = User.objects.all().filter(date_joined__gte=timezone.now()).count()
        return Response(
            {
                "total": total_users,
                "last_week": users_increased
            }
        )

class TonnageIncreasedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
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
    A simple ViewSet for listing or retrieving users.
    """
    def retrieve(self, request):
        return Response(
            {
                "total": 0,
                "last_week": 0
            }
        )
