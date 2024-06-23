from django.db import models

# Create your models here.

class asciiart(models.Model):
    name=models.CharField(max_length=100)
    raw_img=models.ImageField(upload_to='images/')
    art=models.TextField()

    def __str__(self):
        return self.name