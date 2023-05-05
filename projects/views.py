from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Projects(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        # try:
        #      payments= Payment.objects.get(user=request.user)
        # except: payments =  None
        
        # fullstack = Recapsesion.objects.filter(courses__name='Full-Stack Engineering')
        # front_end = Recapsesion.objects.filter(courses__name='Front-end Engineering')
        return render(request, 'dashboard/project.html',{})
       
        
        
    def post(self,request):
        return render(request, 'dashboard/project',{})