from django.urls import path
from .views import Projects, Projects_datials, Payment_approval




urlpatterns = [
    
   
    path('',Projects.as_view(), name='projects'),
    path('project/<int:pk>', Projects_datials.as_view(),name='project_datials'),
    path("payment_approval/",Payment_approval.as_view(), name="payment_approval" )
    
]
