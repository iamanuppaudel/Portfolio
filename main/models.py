from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, null= True, blank= True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200, null= True, blank= True)
    description = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField( null= True, blank= True)
    views = models.IntegerField(default=0, null= True, blank= True)
    github_link = models.CharField(max_length=200, null= True, blank= True)
    demo_link = models.CharField(max_length=200, null= True, blank= True)
    date_added = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


class Blog(models.Model):
    title = models.CharField(max_length=200, null= True, blank= True)
    description = RichTextUploadingField(null=True, blank=True)
    views = models.IntegerField(default=0, null= True, blank= True)
    image = models.ImageField( null= True, blank= True)
    date_added = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(default=0,null=True, blank=True)


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


    
