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
from django.http import JsonResponse
from projects .models import Assigment, Project




# Create your views here.

class Groupscohort(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request, pk):
        mycohorts = Cohorts.objects.filter(pk=pk)
        
        for cohorts in mycohorts:
            mycohort  = cohorts.users.all
        # 'mycohort':mycohort
        try:
            groupcohort = Cohorts.objects.get(users=request.user)
        except:groupcohort = None
        return render(request, 'dashboard/mycohorts.html',{'mycohorts': groupcohort, 'mycohort':mycohort,})
    
    def post(self, request, pk):
        return render(request, 'dashboard/mycohorts.html')
    

class Profileviews(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request, pk):
      myprofile = Profiles.objects.get(pk=pk)
     
      myemail = myprofile.user.email
      return render(request, 'dashboard/profileveiw.html',{'myprofile':myprofile, 'myemail':myemail})
    
    def post(self, request, pk):
        return render(request, 'dashboard/profileveiw.html')



class Profieupdate(LoginRequiredMixin,View):
    login_url = 'login'
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
        uplaod_profile = request.FILES.get('file')
        last_name = request.POST['last_name']
        phone =    request.POST['phone_number']
        
        
        myprofile.git_hub = github
        myprofile.facebook = facebook
        myprofile.twitter =  twitter
        myprofile.youtube  = youtube
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.phone_num = phone
        myprofile.uplaod_picture = uplaod_profile 
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
            assign = Assigment.objects.get(user=request.user)
            if assign.score_project < 15:
                return  redirect('reating')
        except: assign = None


        
        try:
            admission = Profiles.objects.get(user=request.user)
        except: admission = None
        
        fullstack = Livesesion.objects.filter(courses__name='Full-Stack Engineering')
        front_end = Livesesion.objects.filter(courses__name='Front-end Engineering')
        product_design = Livesesion.objects.filter(courses__name='Product Design')
        return render(request, 'dashboard/classroom.html',{'admissionnow':admission,'payments':payments, 'fullstack':fullstack, 'front_end':front_end,'product_design':product_design})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/classroom.html',{})
    
    

class Recapclassroom(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        try:
             payments= Payment.objects.get(user=request.user)
        except: payments =  None

        try:
            assign = Assigment.objects.get(user=request.user)
            if assign.score_project < 15:
                return  redirect('reating')
        except: assign = None
        
        fullstack = Recapsesion.objects.filter(courses__name='Full-Stack Engineering')
        front_end = Recapsesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/recap_classroom.html',{'payments':payments, 'fullstack':fullstack, 'front_end':front_end})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/recap_classroom.html',{})
    
    

class Tasks(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        task =  Task.objects.filter(status='pending')
        return render(request, 'dashboard/newtask.html',{'allcohorts':task })
        
    def post(self,request):
        return render(request, 'dashboard/newtask.html')


class Taskscollection(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request):
        total_task = Task.objects.all().count()
        task_collection =  Task_collections.objects.filter(student=request.user)[:4]
        task =  Task.objects.filter(status='pending', student=request.user)
        approved_task_count = Task_collections.objects.filter(status='approved', student=request.user).count()
        completed_task_count = Task_collections.objects.filter(status='complete', student=request.user).count()
        
        
        context = {
            'total_task': total_task,
            'task': task,
            'task_collection':task_collection,
            'completed_task_count':completed_task_count,
            'approved_task_count':approved_task_count
        }
        
        print(completed_task_count)
        return render(request, 'dashboard/newtask.html', context=context)
    
    from django.http import JsonResponse

        
    def post(self,request):
        try:
            task_collection = request.POST['project']
            link = request.POST['url']
            screen_short = request.FILES.get('myfiles')
            
            submitted_task = Task_collections.objects.filter(task=task_collection, student=request.user).exists()
            if submitted_task:
                return JsonResponse({'success': False, 'error': 'Task already submitted.'})
            else:
                 create_task = Task_collections.objects.create(
                task=task_collection,
                links=link,
                screen_short=screen_short,
                student=request.user,
                status='pending'
            )
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
        
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
        messages.success(request,'Profile Update Successfully')
        return render(request, 'dashboard/social_profile.html')
    
    