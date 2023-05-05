from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Cohorts(models.Model):
    name = models.CharField(max_length=200, unique=True)
    users  = models.ManyToManyField(User)
    
    
    def __str__(self):
        return self.name

payment = (
    ('pending', "pending"),
    ('approved', "approved"),
    ('reject', "reject"),
)

class Payment(models.Model):
    amount = models.CharField(max_length=200)
    courses = models.CharField(max_length=200) 
    payment_type = models.CharField(max_length=200)
    date =      models.CharField(max_length=200)
    uplaod     =   models.ImageField(upload_to='payment')
    user   =     models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=200,choices=payment, default='pending')
    
    def __str__(self):
        return self.courses
    
    
    
    


class Mypasscode(models.Model):
    passcodeNo = models.CharField(max_length=200, unique=True) 
    student = models.ForeignKey(User,on_delete=models.CASCADE)   



      
    

    
    
