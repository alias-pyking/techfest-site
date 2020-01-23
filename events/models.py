from django.db import models
from django.urls import  reverse

def upload_location(instance, filename):
    return '{}/{}'.format(instance, filename)
class Event(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length = 250,null= True,blank = True)
    date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('event_detail',kwargs={'pk':self.pk})

class Star(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.name)
class RegisterEventUsers(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    college_name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)
    registration_id = models.CharField(max_length = 15,default = 'adav123test')

    def __str__(self):
        return str(self.name)
    
    