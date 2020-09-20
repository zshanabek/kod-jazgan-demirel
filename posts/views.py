from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
