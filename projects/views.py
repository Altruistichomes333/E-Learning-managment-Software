from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from dash.models import Payment


# Create your views here.


class Projects(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        # try:
        #      payments= Payment.objects.get(user=request.user)
        # except: payments =  None
        projects = Project.objects.filter(status='active')
        expired_projects = Project.objects.filter(status='expired')
        # fullstack = Recapsesion.objects.filter(courses__name='Full-Stack Engineering')
        # front_end = Recapsesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/project.html',{'projects':projects, 'expired_projects': expired_projects})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/project',{})
    

class Projects_datials(View):
    def get(self,request, pk):
        projects_datials = Project.objects.get(pk=pk)
        expired_projects = Project.objects.filter(status='expired')
        return render(request, 'dashboard/project_details.html', {'projects_datial' :projects_datials, 'expired_projects': expired_projects} )
    
    
    
    def post(self, request, pk):
        projects_datials = Project.objects.get(pk=pk)
        expired_projects = Project.objects.filter(status='expired')
        return render(request, 'dashboard/project_details.html', {' projects_datial': projects_datials})
    
   
   
    
class Payment_approval(View):
    def get(self, request):
        payment_materials = Payment.objects.all()
        return render(request, "dashboard/payment_approval.html", {'payment_materials':payment_materials})
        
        
    def post(self, request):
        return render(request, "dashboard/payment_approval.html")