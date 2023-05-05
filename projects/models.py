from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from dash.models import Payment


# Create your models here.
# title
# start date 
# endate 
# header
# description
# courses

mystatus = (
    ('expired', 'expired'),
     ('active', 'active')
)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    ending_date = models.DateTimeField(auto_created=True)
    start_date = models.DateField(auto_created=True)
    course =   models.ForeignKey(Payment, on_delete=models.CASCADE)
    status =    models.CharField(max_length=200, choices=mystatus, default='yes')
    descriptions = RichTextUploadingField(blank=True)
    
    
    def __str__(self):
        return self.project_name
    
    
    