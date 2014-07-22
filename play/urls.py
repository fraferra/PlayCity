from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from play import views, api

urlpatterns = patterns('',
    url(r'^login/$', views.login ,name='login'),  
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^idea/$', views.idea ,name='idea'),


    url(r'^$', views.index ,name='index'),
    url(r'^(?P<city_name>\w+)/event/$', views.event ,name='event'),
    url(r'^tmp_home/$', views.tmp_home ,name='tmp_home'),
    url(r'^(?P<city_name>\w+)/home/$', views.home ,name='home'),
    url(r'^(?P<city_name>\w+)/look_events/$', views.look_events ,name='look_events'),
    url(r'^(?P<city_name>\w+)/look_coupons/$', views.look_coupons ,name='look_coupons'),
    url(r'^(?P<city_name>\w+)/leaderboard/$', views.leaderboard ,name='leaderboard'),
    url(r'^(?P<city_name>\w+)/feeds/$', views.feeds ,name='feeds'),
    url(r'^(?P<city_name>\w+)/edit_profile/$', views.edit_profile ,name='edit_profile'),

)

