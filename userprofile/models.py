from django.db import models
from django.contrib.auth import get_user_model
from dash.models import Cohorts


User =  get_user_model()






class Social(models.Model):
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    git_hub = models.CharField(max_length=200)
    youtube =  models.CharField(max_length=200)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    


class Profiles(models.Model):
    adminsion_status = (
    ('pending', 'pending'),
    ('rejected', 'rejected'),
    ('admitted', 'admitted')
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    state =    models.CharField(max_length=200)
    city  =    models.CharField(max_length=200)
    local_govt = models.CharField(max_length=200)
    phone_num =  models.CharField(max_length=200)
    contact_add = models.CharField(max_length=600)
    courses =     models.CharField(max_length=300)
    laptop  =   models.CharField(max_length=200)
    certifcate  = models.CharField(max_length=200)
    occupation   =  models.CharField(max_length=200)
    location  =    models.CharField(max_length=200)
    social_media  = models.CharField(max_length=200)
    social_medialink = models.CharField(max_length=300)
    user =     models.ForeignKey(User, on_delete=models.CASCADE)
    status =   models.CharField(max_length=50, choices=adminsion_status, default='pending')
    uplaod_picture =  models.ImageField(upload_to='profile', default=2)
    sponsorship = models.CharField(max_length=200, blank=True, null=True)
    #addtionl information
    facebook = models.CharField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    git_hub = models.CharField(max_length=200,blank=True, null=True)
    youtube =  models.CharField(max_length=200,blank=True, null=True)
    Cohorts    = models.ForeignKey(Cohorts, on_delete=models.CASCADE,blank=True, null=True)
    
    
   
    
# # 
# class Social_Media(models.Model):
#     facebook = models.CharField(max_length=200)
#     twitter = models.CharField(max_length=200)
#     git_hub = models.CharField(max_length=200)
#     youtube =  models.CharField(max_length=200)
    
    
   
