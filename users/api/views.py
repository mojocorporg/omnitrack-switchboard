from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.models import PhoneToken
from .serializers import (
    PhoneTokenCreateSerializer, PhoneTokenValidateSerializer
)
from .utils import user_detail
from django.contrib.auth import get_user_model
import datetime


class GenerateOTP(CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer
    permission_classes = ()

    def post(self, request, format=None):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            token = PhoneToken.create_otp_for_number(
                request.data.get('phone_number')
            )
            if token:
                phone_token = self.serializer_class(
                    token, context={'request': request}
                )
                return Response(phone_token.data)
            return Response({
                'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
                    n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ValidateOTP(CreateAPIView):

    def __init__(self, *args, **kwargs):
        self.user_model = get_user_model()

    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenValidateSerializer
    permission_classes = ()

    def post(self, request, format=None):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            pk = request.data.get("pk")
            otp = request.data.get("otp")
            try:
                timestamp_difference = datetime.datetime.now() - datetime.timedelta(
                    minutes=getattr(settings, 'PHONE_LOGIN_MINUTES', 10)
                )
                phone_token = PhoneToken.objects.get(
                    pk=pk,
                    otp=otp,
                    used=False,
                    timestamp__gte=timestamp_difference
                )
                user = self.user_model.objects.filter(
                    userextra__phone_number=phone_token.phone_number
                ).first()
                phone_token.used = True
                phone_token.attempts += 1
                phone_token.save()
                if user:
                    last_login = user.last_login
                login(request, user)
                response = user_detail(user, last_login)
                return Response(response, status=status.HTTP_200_OK)
            except PhoneToken.DoesNotExist:
                phone_token = PhoneToken.objects.get(pk=pk)
                phone_token.attempts = phone_token.attempts + 1
                phone_token.save()
                raise PhoneToken.DoesNotExist
            except ObjectDoesNotExist:
                return Response(
                    {'reason': "OTP doesn't exist"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
