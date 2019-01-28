from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detail(request, post_id):
    #return HttpResponse("You are reading the detail of post %s" % post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
