from django.db import models

# Create your models here.

class Materials(models.Model):
    name =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Courses(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='coursesimage')
    description = models.TextField(max_length=500)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, default=2)
    
    
    
    def __str__(self):
        return self.title
    
