from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200,blank = True)
    slug = models.CharField(max_length=500, unique=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank = True)
    rank = models.IntegerField()
    ulr = models.URLField(blank= True, max_length=500)
    def __str__(self):
        return self.name