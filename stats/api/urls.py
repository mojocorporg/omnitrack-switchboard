from .viewsets import (
    UserIncreasedViewSet, TonnageIncreasedViewSet, LeadIncreasedViewSet
)
from django.conf.urls import url
from django.urls import path

userincreased = UserIncreasedViewSet.as_view({
    'get': 'retrieve',
})

tonnageincreased = TonnageIncreasedViewSet.as_view({
    "get": "retrieve",
})

leadincreased = LeadIncreasedViewSet.as_view({
    "get": "retrieve",
})

urlpatterns = [
    url(r'^user/$', userincreased),
    url(r'^tonnage/$', tonnageincreased),
    url(r'^lead/$', leadincreased),
]
