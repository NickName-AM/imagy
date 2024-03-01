from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-home'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('like/<int:id>/', views.update_like, name='post-like'),
    path('delete/<int:id>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.PostSearchView.as_view(), name='post-search'),
    path('detail/<int:id>/', views.PostDetailView.as_view(), name='post-detail'),
]