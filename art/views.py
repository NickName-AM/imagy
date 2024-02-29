from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from art.models import Art

# Create your views here.

class ArtListView(ListView):
    model = Art
    template_name = 'art/index.html'
    context_object_name = 'arts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context

class ArtCreateView(CreateView):
    model = Art
    fields = ['title', 'image', 'tags']
    template_name = 'art/create.html'