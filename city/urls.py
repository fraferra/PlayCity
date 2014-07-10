from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from city import views

urlpatterns = patterns('',
    url(r'^test/$', views.test ,name='test'),



)

