from django.shortcuts import render
from django.views.generic import View
from dash.models import Cohorts,Payment
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Livesesion, Recapsesion


# Create your views here.

class Groupscohort(View):
    def get(self, request, pk):
        mycohorts = Cohorts.objects.filter(pk=pk)
        
        for cohorts in mycohorts:
            mycohort  = cohorts.users.all
        # 'mycohort':mycohort
        try:
           groupcohort = Cohorts.objects.get(users=request.user)
        except:  groupcohort = None
        
        
       
             
            
        
      
        
       
        return render(request, 'dashboard/mycohorts.html',{'mycohorts': groupcohort, 'mycohort':mycohort })
    
    def post(self, request, pk):
        return render(request, 'dashboard/mycohorts.html')
    
    
    
class AllCohorts(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        allcohorts = Cohorts.objects.all()
        return render(request, 'dashboard/groups_cohorts.html',{'allcohorts': allcohorts})
        
    def post(self,request):
        return render(request, 'dashboard/groups_cohorts.html')

class Classroom(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        try:
             payments= Payment.objects.get(user=request.user)
        except: payments =  None
        
        fullstack = Livesesion.objects.filter(courses__name='Full-Stack Engineering')
        front_end = Livesesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/classroom.html',{'payments':payments, 'fullstack':fullstack, 'front_end':front_end})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/classroom.html',{})
    
    

class Recapclassroom(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        try:
             payments= Payment.objects.get(user=request.user)
        except: payments =  None
        
        fullstack = Recapsesion.objects.filter(courses__name='Full-Stack Engineering')
        front_end = Recapsesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/recap_classroom.html',{'payments':payments, 'fullstack':fullstack, 'front_end':front_end})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/recap_classroom.html',{})