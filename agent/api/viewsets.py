from rest_framework.response import Response
from rest_framework import viewsets
from agent.models import CommissionAgent
from .serializers import CommissionAgentSerializer


class CommissionAgentViewSet(viewsets.ModelViewSet):
    queryset = CommissionAgent.objects.all()
    serializer_class = CommissionAgentSerializer
