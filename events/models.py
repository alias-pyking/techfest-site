from django.db import models
from django.urls import  reverse

def upload_location(instance, filename):
    return '{}/{}'.format(instance, filename)

class Event(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('event_detail',kwargs={'pk':self.pk})

class Star(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length = 150)
    description = models.TextField()


    def __str__(self):
        return str(self.name)
class RegisterEventUsers(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    college_name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)
    def __str__(self):
        return str(self.name)
    