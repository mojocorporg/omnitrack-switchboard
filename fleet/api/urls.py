from .viewsets import (
    FleetOwnerViewSet, OperationViewSet, FeedViewSet, VehicleViewSet,
    VehicleTypeViewSet, LeadViewSet, QuoteViewSet, JobViewSet, RatingViewSet,
    MaterialTypeViewSet
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


material_type_list = MaterialTypeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

material_type_detail = MaterialTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


vehicletype_list = VehicleTypeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

vehicletype_detail = VehicleTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


lead_list = LeadViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lead_detail = LeadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


quote_list = QuoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

quote_detail = QuoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


job_list = JobViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

job_detail = JobViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


rating_list = RatingViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

rating_detail = RatingViewSet.as_view({
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
    url(r'^operation/$', operation_list),
    url(r'^operation/(?P<pk>[0-9]+)/$$', operation_detail),
    url(r'^feed/$', feed_list),
    url(r'^feed/(?P<pk>[0-9]+)/$$', feed_detail),
    url(r'^vehicle/$', vehicle_list),
    url(r'^vehicle/(?P<pk>[0-9]+)/$$', vehicle_detail),
    url(r'^vehicletype/$', vehicletype_list),
    url(r'^vehicletype/(?P<pk>[0-9]+)/$$', vehicletype_detail),
    url(r'^lead/$', lead_list),
    url(r'^lead/(?P<pk>[0-9]+)/$$', lead_detail),
    url(r'^quote/$', quote_list),
    url(r'^quote/(?P<pk>[0-9]+)/$$', quote_detail),
    url(r'^job/$', job_list),
    url(r'^job/(?P<pk>[0-9]+)/$$', job_detail),
    url(r'^rating/$', rating_list),
    url(r'^rating/(?P<pk>[0-9]+)/$$', rating_detail),
]
