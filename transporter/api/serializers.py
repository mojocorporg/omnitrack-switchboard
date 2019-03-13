from rest_framework import serializers
from transporter.models import Transporter


class TransporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporter
        fields = (
            "id", "transporter", "company_name", "company_address", "phone", "meta"
        )

