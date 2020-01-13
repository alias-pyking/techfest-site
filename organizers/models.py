from django.db import models

# Method to get the upload location for image
# upload location = nameOfInstance/filename
def upload_location(instance, filename):
    return '{}/{}'.format(instance, filename)
class StudentCordinators(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length = 150)
    def __str__(self):
        return str(self.name)
    

class Devs(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length = 150)
    typ = models.CharField(max_length = 150)
    def __str__(self):
        return str(self.name)
class FacultyCordinators(models.Model):
    image = models.ImageField(upload_to = upload_location)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.name)
    
