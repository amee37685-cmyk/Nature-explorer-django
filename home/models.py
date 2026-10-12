from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=112)
    email=models.CharField(max_length=112)
    password=models.CharField(max_length=112)
    country=models.CharField(max_length=112)
    gender=models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return self.name