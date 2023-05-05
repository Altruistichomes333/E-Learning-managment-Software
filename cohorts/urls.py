from django.urls import path
from .views import Groupscohort, AllCohorts,Classroom,Recapclassroom




urlpatterns = [
    
    path('mycohorts/<int:pk>',Groupscohort.as_view(), name='cohorts'),
    path('allcohorts/',AllCohorts.as_view(), name='groupscohort'),
    path('live/',Classroom.as_view(), name='live'),
    path('recap/',Recapclassroom.as_view(), name='recap')
    
]
