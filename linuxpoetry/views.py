"""Simply displays a page and retrieves poems."""

from django.shortcuts import get_object_or_404, render_to_response
from linuxpoetry.models import Post


def index(request, post_id=None):
    """Will return an index page."""
    post = None
    next_id = None
    prev_id = None
    post_count = Post.objects.count()
    if post_count > 0:
        if not post_id:
            post = Post.objects.order_by('-created_at')[0]
        else:
            post = Post.objects.get(id=post_id)
        if post.id < post_count:
            next_id = post.id + 1
        if post.id > 1:
            prev_id = post.id - 1

    return render_to_response(
        'linuxpoetry/base.html',
        {
            'request': request,
            'post': post,
            'next_id': next_id,
            'prev_id': prev_id,
        }
    )
