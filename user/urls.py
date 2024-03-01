from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views


urlpatterns = [
    path('register/', user_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    # path('login/',views.login),
    path('profile/',user_views.profile,name='profile'),
    path('profile/<int:id>/', user_views.user_profile, name='profile-user'),
]


