""" Define URL patterns for team_sports_app"""

from django.conf.urls import url

from . import views

app_name = 'team_sports_app'
urlpatterns = [
	# Home page
	url(r'^$', views.index, name = 'index'),

	# Show all the events
	url(r'^events/$', views.events, name = 'events'),
	
	# Show the details of one selected event
	url(r'^events/(?P<event_id>\d+)/$', views.event, name = 'event'),

	# Add new Event
	url(r'^new_event/$', views.new_event, name='new_event'),
]
