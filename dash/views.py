from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profiles
from django.core.exceptions import ObjectDoesNotExist
from .models import Cohorts
from .models  import Mypasscode
from django.contrib import messages
from .models import Payment
from projects .models import Assigment, Project, Score
from projects .models import  Task_collections
from django.core.mail import send_mail
import pdb
from portal.settings import EMAIL_HOST_USER
from projects.models import Project
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site


# studentcode = None
# cohorts = None
# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    login_url ='login'
    
    def get(self, request):
        myscore = Score.score_caculations(request.user)
        # user = request.user
        # pdb.set_trace()
        
        adimitted_student = Profiles.objects.filter(status='admitted')
        try:
            profile = Profiles.objects.get(user=request.user).first_name
        except ObjectDoesNotExist:
            return  redirect('profile')
        try:
            task_collection =  Task_collections.objects.get(student=request.user)
        except ObjectDoesNotExist:
            return redirect('task_collwction')
        
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
          assigment = Assigment.objects.get(user=request.user)
        except: assigment = None
        
        
        try:
          project = Project.objects.get(user=request.user)
        except: project = None
        
        
        try:
           studentcode = Mypasscode.objects.get(student=request.user).passcodeNo
        except: studentcode = None
        
        try:
           admitted = Profiles.objects.filter(status='admitted')
        except: admitted = None
        
        admitted2 = Profiles.objects.filter(status='admitted')
        
        
       
    
       
    
        
        
        context = {
            'project':project,
            'cohorts':cohorts, 
            'profile':myprofile, 
            'passcode':studentcode,
            'myid':myid,
            'adimitted_student':adimitted_student, 
            'assigment':assigment,
            'myscore': myscore,
            'admitted':admitted,
            
            
        }
        messages.success(request, "Login sucessfully, welcome")
        return render(request, 'dashboard/dash.html', context=context)
    
    def post(self, request):
        return render(request, 'dashboard/dash.html')
    
    
    
    
    
   #this is code line for approved view  
def approved(request, pk):
    payment_approved = Payment.objects.get(pk=pk)
    

    payment_approved.payment_status = 'approved'
    payment_approved.mysave()
    payment_approved.save()
    subject = "Payment Approved"
    body = "hello payment has being approved"
    from_email = EMAIL_HOST_USER
    toemail =  [payment_approved.user.email]
    send_now =send_mail(subject, body,from_email, toemail)
    if send_now:
        messages.success(request, "email sent to user sucessfully ")
    
    messages.success(request, "payment appoved sucessful")
    return redirect('payment_approval')



class Pending_student(View):
    def get(self, request):
        pending_approval = Profiles.objects.filter(status="pending")
        return render(request, "dashboard/adminssion_approval.html", {'pending_approval':pending_approval})
        
        
    def post(self, request):
        return render(request, "dashboard/adminssion_approval.html")


def approved_admission(request, pk):
    admissioin_approved = Profiles.objects.get(pk=pk)
    admissioin_approved.status = 'admitted'
    admissioin_approved.save()
    subject = "Congratulations, you’ve been accepted to the Obidients Tech Space for Software Engineering Programme"
    text = "Welcome "
    from_email = EMAIL_HOST_USER
    toemail =  [admissioin_approved.user.email]
    current_site = get_current_site(request)
    context = {
        
        'admissioin_approved':admissioin_approved ,
        'current_site':   current_site
    }
    
    html_message = render_to_string(
                    template_name='dashboard/email.html', context=context)
    mysend = EmailMultiAlternatives( subject, text, from_email, toemail)
    mysend.attach_alternative(html_message, 'text/html')
    mysend.send()
    
    # send_now =send_mail(subject, body,from_email, toemail)
    # if send_now:
    #     messages.success(request, "email sent to user sucessfully ")
    
    messages.success(request, "email sent to user sucessfully")
    return redirect('pending')



def myapproved(request, pk):
    assign = Assigment.objects.get(pk=pk)
    assign.status = 'complete'
    assign.save()
    return redirect('assigment_approval')




def approved_myproject(request, pk):
    project_approved = Project.objects.get(pk=pk)
    project_approved.status = "active"
    project_approved.save()
    admitted = Profiles.objects.filter(status='admitted')
    subject = "A new project is now available"
    from_email = EMAIL_HOST_USER
    text = "Welcome "
    current_site = get_current_site(request)
    context = {
        
        'project':project_approved ,
        'current_site':   current_site
    }
    html_message = render_to_string(
                    template_name='dashboard/email_project.html', context=context)
    
  
        
    for admit in admitted:
        toemail = admit.user.email
        mysend = EmailMultiAlternatives( subject, text, from_email, [toemail])
        mysend.attach_alternative(html_message, 'text/html')
        mysend.send()
        # send_mail(subject, body,from_email, [toemail])
    messages.success(request, "email sent to user sucessfully ")
    return redirect('pending')


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
        
       