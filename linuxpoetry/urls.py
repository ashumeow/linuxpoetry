"""/<poem_id> returns json for some poem object."""

from django.conf.urls import patterns, url
from linuxpoetry import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.index, name='post'),
    url(r'^json/(?P<post_id>\d+)/$', views.get_json_post, name='json_post'),
)
