from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
from ckeditor.fields import RichTextField
from django_quill.fields import QuillField
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=600)
    auther = models.CharField(max_length=50)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    descriptions = QuillField()
    image = models.ImageField(upload_to='blog')

    is_published = models.BooleanField(default=True)
    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title} By {self.auther}'

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'Comment By {self.name}'