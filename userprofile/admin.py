from django.contrib import admin
from .models import Profiles

# Register your models here.
@admin.register(Profiles)
class Profile(admin.ModelAdmin):
    list_display = ('first_name',  'last_name', 'state', 'phone_num', 'status','Cohorts','facebook','twitter','git_hub','youtube' )




# # Register your models here.
# @admin.register(Social)
# class Socila_media(admin.ModelAdmin):
#     list_display = ('facebook','twitter','git_hub','youtube','user')
