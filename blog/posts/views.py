from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post


# Create your views here.

def index(request):
    return render(request, 'index.html', {'posts': Post.get_all_posted_posts()})
