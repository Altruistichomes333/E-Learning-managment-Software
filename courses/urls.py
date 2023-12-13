from django.urls import path
from django.contrib import admin
from .views import MyCourses, Materialspayment,Paymentslips,Gen, Edit_Liveclass,UpdateMaterials



urlpatterns = [
    
    path('', MyCourses.as_view(),name="courses"),
    path('payment', Materialspayment.as_view(), name='payment'),
    path('slips', Paymentslips.as_view(), name='slips'),
    path('generate',Gen.as_view(), name='gen'),
    path('edit_live/<int:pk>',Edit_Liveclass.as_view(), name='edit_live'),
    path('updated/<int:pk>',UpdateMaterials.as_view(), name='updated'),
    
]
