from .viewsets import (
    CityViewSet, StateViewSet, CountryViewSet
)
from django.conf.urls import url
from django.urls import path


city_list = CityViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

city_detail = CityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


state_list = StateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

state_detail = StateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


country_list = CountryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

country_detail = CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^city/$', city_list),
    url(r'^city/(?P<pk>[0-9]+)/$$', city_detail),
    url(r'^state/$', state_list),
    url(r'^state/(?P<pk>[0-9]+)/$$', state_detail),
    url(r'^country/$', country_list),
    url(r'^country/(?P<pk>[0-9]+)/$$', country_detail),
]
