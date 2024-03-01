from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from post.models import Post

from django.contrib.auth.models import User

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'tags']
    template_name = 'post/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == product.user:
            return True
        return False

@login_required
def update_like(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        user = User.objects.get(id=request.user.id)
        # print(post.liked_by.split(' '))
        if user.username not in post.liked_by.split(' '):
            post.liked_by += f' {user.username}'
            post.save()
            post.likes += 1
            post.save()
    
    return redirect('post-home')

class PostSearchView(ListView):
    model = Post
    template_name = 'post/search.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_data = self.request.GET['search-data']
        posts = Post.objects.all()
        filtered = []
        for post in posts:
            t = post.tags.split(' ')
            if search_data in t:
                filtered.append(post)
        
        print(filtered)

        return context