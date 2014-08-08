from django.conf.urls import patterns, include, url
#from tastypie.api import Api
#from play.api.resources import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^play_palo_alto/', include('play_palo_alto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'', include('play_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('play.urls', namespace="play")),
    url(r'^(?P<city_name>\w+)/charity/', include('charity.urls', namespace="charity")),
    url(r'^(?P<city_name>\w+)/', include('city.urls', namespace="city")),
    url(r'^(?P<city_name>\w+)/shop/', include('shop.urls', namespace="shop")),
    url(r'^', include('city.urls', namespace="city")),
    url(r'', include('social_auth.urls')),
    #(r'^api/', include('play.api_urls', namespace="api")),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
)
