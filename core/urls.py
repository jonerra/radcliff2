from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^player_registration/$', PlayerRegistration.as_view(), name='player_registration'),
    url(r'^volunteer_registration/$', VolunteerRegistration.as_view(), name='volunteer_registration'),
    url(r'^success/$', Success.as_view(), name='success'),
    url(r'^reservation_success/$', FieldReservationSuccess.as_view(), name='reservation_success'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^roster/$', PlayerRoster.as_view(), name='player_roster'),
    url(r'^update/create/$', LeagueUpdate.as_view(), name='update_create'),
    url(r'^league/$', UpdateList.as_view(), name='update_list'),
    url(r'^fields/$', FieldList.as_view(), name='field_list'),
    url(r'^fields/(?P<pk>\d+)/$', FieldDetail.as_view(), name='field_detail'),
    url(r'^fields/create/$', FieldReservationCreateView.as_view(), name='field_create'),
    url(r'^fields/update/(?P<pk>\d+)/$', FieldReservationUpdateView.as_view(), name='field_update'),
    url(r'^roster/(?P<pk>\d+)/$', PlayerInfoDetailView.as_view(), name='player_detail'),
)