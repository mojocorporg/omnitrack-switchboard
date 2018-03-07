from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer
from agent.models import CommissionAgent
from rest_framework import serializers


class CAAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        attrs = super(CAAuthTokenSerializer, self).validate(attrs)
        user = attrs.get("user")
        try:
            user.commissionagent
        except:
            msg = _('Login as a commission agent.')
            raise serializers.ValidationError(msg, code='authorization')
        return attrs
