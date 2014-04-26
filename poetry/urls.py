import os

from django.conf.urls import patterns, include, url
import linuxpoetry.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include(linuxpoetry.urls)),
)

if os.environ.get('POETRY_ADMIN') == '1':
    urlpatterns += url(r'^manage/admin/', include(admin.site.urls)),
