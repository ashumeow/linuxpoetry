from django.conf.urls import patterns, include, url
import linuxpoetry.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plus.views.home', name='home'),
    # url(r'^plus/', include('plus.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
  url(r'^manage/admin/', include(admin.site.urls)),
  url(r'^', include(linuxpoetry.urls)),
)
