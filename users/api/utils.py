from rest_framework import status
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from agent.api.serializers import CommissionAgentSerializer
from fleet.api.serializers import FleetOwnerSerializer

STATUS = {
    "status": None,
    "message": None,
}


def too_many_requests():
    STATUS["status"] = status.HTTP_429_TOO_MANY_REQUESTS
    STATUS["message"] = "Reached max limit for the day."
    return (STATUS, STATUS["status"])


def unauthorized():
    STATUS["status"] = status.HTTP_401_UNAUTHORIZED
    STATUS["message"] = "User not logged in."
    return (STATUS, STATUS["status"])


def failure(message="Failed"):
    STATUS["status"] = status.HTTP_400_BAD_REQUEST
    STATUS["message"] = message
    return (STATUS, STATUS["status"])


def success(message=None):
    STATUS["status"] = status.HTTP_200_OK
    STATUS["message"] = message
    return (STATUS, STATUS["status"])


def user_detail(user, last_login):
    try:
        token = user.auth_token.key
    except:
        token = Token.objects.create(user=user)
        token = token.key
    try:
        ca = CommissionAgentSerializer(user.commissionagent).data()
    except ObjectDoesNotExist:
        ca = dict()
    try:
        fo = FleetOwnerSerializer(user.fleetowner).data()
    except ObjectDoesNotExist:
        fo = dict()
    user_json = {
        "id": user.pk,
        "last_login": last_login,
        "token": token,
        "status": status.HTTP_200_OK,
        "user": {
            "id": user.pk,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": str(user.userextra.phone_number),
            "is_active": user.is_active,
            "date_joined": user.date_joined
        },
        "ca": ca,
        "fo": fo
    }
    return user_json


def model_field_attr(model, model_field, attr):
    """
    Returns the specified attribute for the specified field on the model class.
    """
    fields = dict([(field.name, field) for field in model._meta.fields])
    return getattr(fields[model_field], attr)
