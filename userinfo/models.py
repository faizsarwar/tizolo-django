from django.db import models

# Create your models here.
class info(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    Phone_number= models.CharField(max_length=255)
    email= models.EmailField()
    message= models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
