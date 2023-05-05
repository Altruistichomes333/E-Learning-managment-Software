from django.urls import path
from .views import Projects




urlpatterns = [
    
   
    path('',Projects.as_view(), name='projects')
    
]
