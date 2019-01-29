from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.

def post_list(request, page_id):
# Change the value of postPerPage to define no of post per page
    postPerPage = 3
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[page_id*postPerPage+0:page_id*postPerPage+postPerPage]

    page_id_next = page_id + 1;

    if len(Post.objects.all())/postPerPage <= page_id+1:
        page_id_next = 0

    page_id_prev = page_id - 1
    return render(request, 'blog/post_list.html', {'posts': posts, 'page_id_next':page_id_next, 'page_id_prev':page_id_prev})

def detail(request, post_id):
    #return HttpResponse("You are reading the detail of post %s" % post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
