from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Pages(models.Model):
    title = models.CharField(max_length=100)
    resume = RichTextField()
    content = RichTextUploadingField()
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_create']
