from django.contrib import admin
from .models import Cohorts,Payment, Mypasscode
# Register your models here.
@admin.register(Cohorts)
class Cohorts(admin.ModelAdmin):
    # list_display = ('name', 'users')
    pass

@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ('amount', 'courses')
    
@admin.register(Mypasscode)
class passcode(admin.ModelAdmin):
    list_display = ('passcodeNo', 'student')
   
