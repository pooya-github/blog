from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    topic = models.CharField(max_length=250)
    secondtopic = models.CharField(max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    message = models.TextField()
    tag = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post', blank=True)
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.topic + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))