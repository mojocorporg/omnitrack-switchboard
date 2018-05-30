from .viewsets import (
    UserIncreasedViewSet, TonnageIncreasedViewSet, LeadIncreasedViewSet, TopDestinationViewSet,
    TopSourceViewSet
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

topdestination = TopDestinationViewSet.as_view({
    "get": "list",
})

topsource = TopSourceViewSet.as_view({
    "get": "list",
})

urlpatterns = [
    url(r'^user/$', userincreased),
    url(r'^tonnage/$', tonnageincreased),
    url(r'^lead/$', leadincreased),
    url(r'^destination/list$', topdestination),
    url(r'^source/list$', topsource),
]
