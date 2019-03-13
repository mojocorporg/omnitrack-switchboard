from .viewsets import TransporterViewSet
from django.conf.urls import url
from django.urls import path


transporter_list = TransporterViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

transporter_detail = TransporterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^transporter/$', transporter_list),
    url(r'^transporter/(?P<pk>[0-9]+)/$$', transporter_detail),
]
