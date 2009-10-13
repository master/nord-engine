# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    ('edit/(?P<name>.*)$', 'edit'),
    ('delete/(?P<name>.*)$', 'delete'),                       
    ('(?P<name>.*)$', 'dispatch'),
    ('^$', 'dispatch'),
)
