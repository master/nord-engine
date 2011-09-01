from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^administrate/(.*)', admin.site.root),
    (r'^splash', include('splash.urls')),
    (r'^', include('wiki.urls')),
)
