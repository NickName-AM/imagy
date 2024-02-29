from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from post.models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'image', 'tags']
    template_name = 'post/create.html'