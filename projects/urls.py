from django.urls import path
from .views import Projects, Projects_datials, Payment_approval,view_payment,Submitassigment, Assigment_approval,Pending_payment

from dash.views import myapproved


urlpatterns = [
    
   
    path('',Projects.as_view(), name='projects'),
    path('project/<int:pk>', Projects_datials.as_view(),name='project_datials'),
    path("pending_payment/",Payment_approval.as_view(), name="payment_approval" ),
     path("payment_approval/",Pending_payment.as_view(), name="pending_payment" ),
    path('view/<int:pk>', view_payment.as_view(),name='view_payment'),
    path('submitassigment', Submitassigment.as_view(),name='submitassigment'),
    path('assigment_approval', Assigment_approval.as_view(),name='assigment_approval'),
    
    path('approved/<int:pk>',myapproved, name='assigment_approved')
    
    
]
