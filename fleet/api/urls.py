from .viewsets import (
    FleetOwnerViewSet, CommissionAgentViewSet,
    OperationViewSet, FeedViewSet, VehicleViewSet
)
from django.conf.urls import url
from django.urls import path


fleet_owner_list = FleetOwnerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

fleet_owner_detail = FleetOwnerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


commission_agent_list = CommissionAgentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

commission_agent_detail = CommissionAgentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


operation_list = OperationViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

operation_detail = OperationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


feed_list = FeedViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

feed_detail = FeedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


vehicle_list = VehicleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

vehicle_detail = VehicleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^fleet_owner/$', fleet_owner_list),
    url(r'^fleet_owner/(?P<pk>[0-9]+)/$$', fleet_owner_detail),
    url(r'^commission_agent/$', commission_agent_list),
    url(r'^commission_agent/(?P<pk>[0-9]+)/$$', commission_agent_detail),
    url(r'^operation/$', operation_list),
    url(r'^operation/(?P<pk>[0-9]+)/$$', operation_detail),
    url(r'^feed/$', feed_list),
    url(r'^feed/(?P<pk>[0-9]+)/$$', feed_detail),
    url(r'^vehicle/$', vehicle_list),
    url(r'^vehicle/(?P<pk>[0-9]+)/$$', vehicle_detail),
]
