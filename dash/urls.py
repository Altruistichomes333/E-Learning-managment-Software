from django.urls import path
from .views import   Dashboard, approved



urlpatterns = [
    path('', Dashboard.as_view(), name='dash'),
    path('approved/<int:pk>',approved, name='myapproved'),
   
    # path('passcode', Passcode.as_view(), name='passcode')
    
]
