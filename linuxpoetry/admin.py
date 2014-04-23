"""Enable automatic admin pages for linuxpoetry."""

from django.contrib import admin

from linuxpoetry.models import Post, PostTag

admin.site.register(Post)
admin.site.register(PostTag)
