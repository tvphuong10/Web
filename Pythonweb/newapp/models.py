from django.db import models

# Create your models here.
class data(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=20)
    num_of_steps = models.IntegerField(default=0)
    steps_address = models.CharField(max_length=100)

class steps(models.Model):
    step = models.CharField(max_length=300)
    image = models.ImageField(null= True, blank= True, upload_to="images/")