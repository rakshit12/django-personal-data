from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=100)
    discription= models.TextField(max_length=250)
    image=models.ImageField(upload_to="personal_data/images/")
    url=models.URLField(blank=True)
