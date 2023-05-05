from django.contrib import admin
from .models import Project
# Register your models here.
@admin.register(Project)
class Student_Project(admin.ModelAdmin):
    list_display = ('project_name','course','ending_date','start_date','descriptions', 'status')
     