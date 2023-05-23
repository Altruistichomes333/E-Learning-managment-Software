from django.shortcuts import render, redirect
from django.views.generic import View
from dash.models import Cohorts,Payment
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Livesesion, Recapsesion, Ourteam
from projects .models import Task, Task_collections
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from userprofile .models import Profiles,Social
import pdb




# Create your views here.

class Groupscohort(View):
    def get(self, request, pk):
        mycohorts = Cohorts.objects.filter(pk=pk)
        
        for cohorts in mycohorts:
            mycohort  = cohorts.users.all
        # 'mycohort':mycohort
        try:
            groupcohort = Cohorts.objects.get(users=request.user)
        except:groupcohort = None
        return render(request, 'dashboard/mycohorts.html',{'mycohorts': groupcohort, 'mycohort':mycohort })
    
    def post(self, request, pk):
        return render(request, 'dashboard/mycohorts.html')
    

class Profileviews(View):
    def get(self, request, pk):
      myprofile = Profiles.objects.get(pk=pk)
     
      myemail = myprofile.user.email
      return render(request, 'dashboard/profileveiw.html',{'myprofile':myprofile, 'myemail':myemail})
    
    def post(self, request, pk):
        return render(request, 'dashboard/profileveiw.html')



class Profieupdate(View):
    def get(self, request, pk):
      myprofile = Profiles.objects.get(pk=pk)
     
      return render(request, 'dashboard/updateprofile.html',{'myprofile':myprofile})
    
    def post(self, request, pk):
        myprofile = Profiles.objects.get(pk=pk)
        github = request.POST['github']
        facebook = request.POST['facebook']
        twitter  = request.POST['twitter']
        youtube  = request.POST['youtube']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone =    request.POST['phone_number']
        myprofile.git_hub = github
        myprofile.facebook = facebook
        myprofile.twitter =  twitter
        myprofile.youtube  = youtube
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.phone_num = phone
        myprofile.save()
        messages.success(request, 'income updated sucessfully ')
        return redirect('dash')
        
    
        
        
        
        
         
        
        return render(request, 'dashboard/updateprofile.html')

    
    
class AllCohorts(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        try:
           mycohorts = Cohorts.objects.get(users=request.user)
        except:  mycohorts = None
        allcohorts = Cohorts.objects.all()
        return render(request, 'dashboard/groups_cohorts.html',{"mycohorts":mycohorts, 'allcohorts': allcohorts})
        
    def post(self,request):
        return render(request, 'dashboard/groups_cohorts.html')

class Classroom(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        try:
             payments= Payment.objects.get(user=request.user)
        except: payments =  None
        
        try:
            admission = Profiles.objects.get(user=request.user)
        except: admission = None
        
        fullstack = Livesesion.objects.filter(courses__name='Full-Stack Engineering')
        front_end = Livesesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/classroom.html',{'admissionnow':admission,'payments':payments, 'fullstack':fullstack, 'front_end':front_end})
       
        
        
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
    
    

class Tasks(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        task =  Task.objects.filter(status='pending')
        return render(request, 'dashboard/task.html',{'allcohorts':task })
        
    def post(self,request):
        return render(request, 'dashboard/task.html')


class Taskscollection(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request):
        task =  Task.objects.filter(status='pending')
        
        
        context = {
            
            'task': task
            
        }
        return render(request, 'dashboard/task_collection.html',context=context)
        
    def post(self,request):
        task_collection = request.POST['project']
        link = request.POST['url']
        screen_short = request.FILES.get('myfiles')
        create_task = Task_collections.objects.create( task=task_collection,links=link,
        screen_short=screen_short,student=request.user)
        create_task.status = 'pending'
        create_task.save()
        messages.success(request, 'task submitted successfully pending verification')
        return redirect('task_collwction')
        
        # return render(request, 'dashboard/task_collection.html')

class Ourcommunity(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        
        community = Ourteam.objects.all()
        return render(request, 'dashboard/ourteam.html',{'community':community})
        
    def post(self,request):
        return render(request, 'dashboard/ourteam.html')



class Social_Profile(View):
    def get(self, request):
        try:
            login_profile = Social.objects.get(user=request.user)
        except: login_profile = None
        
            
        # login_profile = Social.objects.get(user=request)
        return render(request, 'dashboard/social_profile.html',{'login_profile':login_profile})
    
    
    def post(self, request):
        github = request.POST['github']
        facebook = request.POST['facebook']
        twitter  = request.POST['twitter']
        youtube  = request.POST['youtube']
        profile_socila = Social.objects.create(facebook=facebook,twitter=twitter,git_hub=github,youtube=youtube,user=request.user)
        profile_socila.save()
        messages.success(request,'Profile Update Sucessfully')
        return render(request, 'dashboard/social_profile.html')
    
    