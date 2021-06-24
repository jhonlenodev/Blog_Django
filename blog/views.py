from django.shortcuts import render
from blog.models import Pages

def home(request):
    posts = Pages.objects.all()
    return render(request, 'home.html', {'posts':posts})

def post(request, post_id):
    post = Pages.objects.get(pk=post_id)
    return render(request, 'post.html', {'post':post})
