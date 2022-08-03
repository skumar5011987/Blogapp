from django.db import models


class Post(models.Model):    
    title = models.CharField(max_length=200)
    uname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
