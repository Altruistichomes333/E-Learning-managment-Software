from django.urls import path
from .views import Groupscohort, AllCohorts,Classroom,Recapclassroom,Tasks,Taskscollection




urlpatterns = [
    
    path('mycohorts/<int:pk>',Groupscohort.as_view(), name='cohorts'),
    path('allcohorts/',AllCohorts.as_view(), name='groupscohort'),
    path('live/',Classroom.as_view(), name='live'),
    path('recap/',Recapclassroom.as_view(), name='recap'),
    path('task/',Tasks.as_view(), name='task'),
    path('task_collection/',Taskscollection.as_view(), name='task_collwction')
    
]
