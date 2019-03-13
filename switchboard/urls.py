"""switchboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse, re_path
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views as authtoken_views
from rest_framework_swagger.views import get_swagger_view
from .views import get_auth_token
from django.conf import settings

admin.site.site_title = "Switchboard Site Admin"
admin.site.site_header = "Switchboard Administration"

urlpatterns = [
    path('', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('fleet/', include('fleet.urls')),
    path('common/', include('common.urls')),
    path('agent/', include('agent.urls')),
    path('stats/', include('stats.urls')),
    path('users/', include('users.urls')),
    path('transporter/', include('transporter.urls')),
]

# Auth Token URL's
urlpatterns.append(
    path('api-token-auth/', get_auth_token)
)
#
## Phone Login
#urlpatterns.append(
#    path('phone_login/', include('phone_login.urls'), name='phone_login')
#)

schema_view = get_swagger_view(title='Switchboard API')

urlpatterns.append(
    path('docs/', schema_view)
)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
