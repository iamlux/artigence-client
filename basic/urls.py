from django.conf.urls import patterns, include, url

from django.contrib import admin
from smartjira.views import *
from django.conf import settings
import django.views.static as django_static_view
admin.autodiscover()

urlpatterns = (
    # Examples:
    # url(r'^$', 'basic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^list', list, name='list')
)


# url(r'^$', home, name='home'),