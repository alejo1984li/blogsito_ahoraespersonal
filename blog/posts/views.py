from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'Posts/posts_page.html', context)