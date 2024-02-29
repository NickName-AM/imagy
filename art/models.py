from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Art(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='Name of the art')
    image = models.ImageField(upload_to='art')
    likes = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length= 200, help_text='Tags (Separated by space. Example: #nature #waterfall)')

    def get_absolute_url(self):
        return reverse('art-home')