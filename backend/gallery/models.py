from django.db import models

# Create your models here.
class Abstract(models.Model):
    src = models.ImageField(upload_to='abstract')
    thumbnail = models.ImageField(upload_to='abstract')
    thumbnailWidth = models.IntegerField()
    thumbnailHeight = models.IntegerField()
    margin = models.IntegerField(default=2)


class Scenic(models.Model):
    src = models.ImageField(upload_to='scenic')
    thumbnail = models.ImageField(upload_to='scenic')
    thumbnailWidth = models.IntegerField()
    thumbnailHeight = models.IntegerField()
    margin = models.IntegerField(default=2)   

class Street(models.Model):
    src = models.ImageField(upload_to='street')
    thumbnail = models.ImageField(upload_to='street')
    thumbnailWidth = models.IntegerField()
    thumbnailHeight = models.IntegerField()
    margin = models.IntegerField(default=2)    

class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.TextField()        