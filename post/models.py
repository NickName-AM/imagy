from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='Title of the post')
    image = models.ImageField(upload_to='post')
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length= 200, help_text='Tags (Separated by space. Example: #nature #waterfall)')

    def get_absolute_url(self):
        return reverse('post-home')