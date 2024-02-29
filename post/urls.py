from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-home'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
]