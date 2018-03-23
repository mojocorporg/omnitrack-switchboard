from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CAAuthTokenSerializer
from agent.api.serializers import CommissionAgentSerializer

class GetAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CAAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        ca = CommissionAgentSerializer(user.commissionagent)
        (user.__dict__).pop("_state")
        (user.__dict__).pop("backend")
        (user.__dict__).pop("password")
        return Response(
            {
                "token": token.key,
                "user": user.__dict__,
                "ca": ca.data
            }
        )


get_auth_token = GetAuthToken.as_view()
