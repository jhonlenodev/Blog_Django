from django.db import models
from django.contrib.auth.models import User

class Pages(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=200)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['date_create']