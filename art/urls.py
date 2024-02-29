from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ArtListView.as_view(), name='art-home'),
    path('create/', views.ArtCreateView.as_view(), name='art-create'),
]