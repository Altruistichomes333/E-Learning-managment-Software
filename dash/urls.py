from django.urls import path
from .views import   Dashboard, approved, approved_admission,Pending_student,approved_myproject



urlpatterns = [
    path('', Dashboard.as_view(), name='dash'),
    path('approved/<int:pk>',approved, name='myapproved'),
    path('approved_admission/<int:pk>',approved_admission, name='admission'),
    path('pending_approval/',Pending_student.as_view(), name='pending'),
    path('approved_admin/<int:pk>',approved_myproject, name='aproved_admin')
   
   
    # path('passcode', Passcode.as_view(), name='passcode')
    
]
