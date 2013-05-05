#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
admin.site.unregister(Site)  #如此在admin站点中禁用掉Site和Group
admin.site.unregister(Group)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeeart.views.home', name='home'),
    # url(r'^jeeart/', include('jeeart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','home.views.index_all'),

    url(r'^blog/$','blog.views.index'),
    url(r'^blog/cat/(?P<cat_id>\d+)/$','blog.views.index'),
    url(r'^blog/p/(?P<page_num>\d+)/$','blog.views.index'),
    url(r'^blog/cat/(?P<cat_id>\S+)/p/(?P<page_num>\d+)/$','blog.views.index'),
    #url(r'^blog/(\d+)/$','blog.views.detail'),

    url(r'^dispic/$', 'dispic.views.index'),
    url(r'^dispic/download/$', 'dispic.views.coming'),
    
    #ajax cgi
    url(r'^cgi/dispic/submit_email', 'dispic.views.submitEmail'),
)

#if True:
if settings.DEBUG:
    urlpatterns += patterns("",
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,"show_indexes":True}),      
)   
