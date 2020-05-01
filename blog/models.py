from django.db import models

# Create your models here.
class project1(models.Model):
    title=models.CharField(max_length=100)
    date= models.CharField(max_length=100)
    discription= models.TextField(max_length=1000)

    def __str__(self):
        return self.title
