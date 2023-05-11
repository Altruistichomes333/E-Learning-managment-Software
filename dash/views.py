from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profiles
from django.core.exceptions import ObjectDoesNotExist
from .models import Cohorts
from .models  import Mypasscode
from django.contrib import messages
from .models import Payment

# studentcode = None
# cohorts = None
# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    login_url ='login'
    
    def get(self, request):
        
        adimitted_student = Profiles.objects.filter(status='admitted')
        try:
            profile = Profiles.objects.get(user=request.user).first_name
        except ObjectDoesNotExist:
            return  redirect('profile')
        
        try:
            cohorts = Cohorts.objects.get(users=request.user).name
        except: cohorts = None
        
        try:
            myid = Cohorts.objects.get(users=request.user)
        except: myid = None
        try:
           myprofile = Profiles.objects.get(user=request.user)
        except: myprofile = None
        
        
        try:
           studentcode = Mypasscode.objects.get(student=request.user).passcodeNo
        except: studentcode = None
        messages.success(request, "Login sucessfully, welcome")
        return render(request, 'dashboard/dash.html',{'cohorts':cohorts, 'profile':myprofile, 'passcode':studentcode,'myid':myid, 'adimitted_student':adimitted_student})
    
    def post(self, request):
        return render(request, 'dashboard/dash.html')
    
    
    
    
    
   #this is code line for approved view  
def approved(request, pk):
    payment_approved = Payment.objects.get(pk=pk)
    payment_approved.payment_status = 'approved'
    payment_approved.mysave()
    payment_approved.save()
    return redirect('dash')
    
    
    
    
    
    
    




#     try:
#         profile = Profiles.objects.get(user=request.user).first_name
#     except ObjectDoesNotExist:
#         return  redirect('profile')
    
#     # context = {
#     #     'cohorts': cohorts
#     # }
    
#     return render(request, 'dashboard/dash.html',{'cohorts':cohorts})
        
# def dashboard(request):
   
   
    
    
#     profileexist = Profiles.objects.filter(user= request.user).exists()
#     passcodeexist = Mypasscode.objects.filter(student=request.user).exists()
#     cohortsexist = Cohorts.objects.filter(users=request.user).exists()
    
#     if passcodeexist:
#         studentcode = Mypasscode.objects.get(student=request.user).passcodeNo
        
#     if profileexist:
#         myprofile = Profiles.objects.get(user=request.user)
    
    
#     if cohortsexist:
#          cohorts = Cohorts.objects.get(users=request.user).name
#          return cohorts

# profileexist = Profiles.objects.filter(user= request.user).exists()
        # passcodeexist = Mypasscode.objects.filter(student=request.user).exists()
        # cohortsexist = Cohorts.objects.filter(users=request.user).exists()
        
        # if passcodeexist:
            
            
          
        #     studentcode = Mypasscode.objects.get(student=request.user).passcodeNo
        
            
        
        # if profileexist:
        #      myprofile = Profiles.objects.get(user=request.user)
        
        
        # if cohortsexist:
        #     cohorts = Cohorts.objects.get(users=request.user).name
        
       