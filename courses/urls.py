from django.urls import path
from django.contrib import admin
from .views import MyCourses, Materialspayment,Paymentslips,Gen


urlpatterns = [
    
    path('', MyCourses.as_view(),name="courses"),
    path('payment', Materialspayment.as_view(), name='payment'),
    path('slips', Paymentslips.as_view(), name='slips'),
    path('generate',Gen.as_view(), name='gen')
    
]
