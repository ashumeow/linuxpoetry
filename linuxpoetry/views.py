"""Simply displays a page and retrieves poems."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from linuxpoetry.models import Post, PostTag
import json


def index(request, post_id=None):
    """Will return an index page."""
    if not post_id:
        post = Post.objects.order_by('-created_at')[0]
    else:
        post = Post.objects.get(id=post_id)
    return render_to_response(
        'linuxpoetry/base.html',
        {
            'request': request,
            'post_id': post.id,
            'post': post,
            'tags': PostTag.objects.all().values_list('name')
        }
    )


def get_json_post(request, post_id=None):
    """Will return an HttpResponse with a json poem."""
    _return = dict()
    post = get_object_or_404(Post, id=post_id)

    _return['title'] = post.title
    _return['body'] = post.body_with_html
    _return['tags'] = [tag.name for tag in post.tags.all()]
    _return['created_at'] = post.created_at.strftime('%m-%d-%Y')
    _return['updated_at'] = post.updated_at.strftime('%m-%d-%Y')

    # Try pulling out the prev/next posts in the series
    prev_post = Post.objects.filter(
        created_at__lt=post.created_at).order_by('-created_at')
    if prev_post:
        _return['prev_post_id'] = prev_post[0].id

    next_post = Post.objects.filter(
        created_at__gt=post.created_at).order_by('created_at')
    if next_post:
        _return['next_post_id'] = next_post[0].id

    return HttpResponse(json.dumps(_return))
