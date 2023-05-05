from django.contrib import admin
from .models import Courses, Materials

# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'material')


@admin.register(Materials)
class Materialadmin(admin.ModelAdmin):
    list_display = ('name',)