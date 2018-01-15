from .viewsets import CommissionAgentViewSet
from django.conf.urls import url
from django.urls import path


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


urlpatterns = [
    url(r'^commission_agent/$', commission_agent_list),
    url(r'^commission_agent/(?P<pk>[0-9]+)/$$', commission_agent_detail),
]
