from rest_framework import serializers
from agent.models import CommissionAgent


class CommissionAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionAgent
        fields = ("id", "agent", "phone", "hub", "meta")
