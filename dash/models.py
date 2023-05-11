from django.db import models
from django.contrib.auth import get_user_model
import random
import string
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
    passcode =    models.CharField(max_length=20)
    payment_status = models.CharField(max_length=200,choices=payment, default='pending')
    
    def __str__(self):
        return self.courses
    
    def mysave(self, *args, **kwargs):
        if self.payment_status == 'approved' and not self.passcode:
            self.passcode = "".join(random.choices(string.ascii_uppercase,k=10))
        super().save(*args, **kwargs)
            
            
        
    
    
    
    


class Mypasscode(models.Model):
    passcodeNo = models.CharField(max_length=200, unique=True) 
    student = models.ForeignKey(User,on_delete=models.CASCADE)   



      
    

    
    
