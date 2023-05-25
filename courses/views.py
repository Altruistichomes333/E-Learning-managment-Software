from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Materials, Courses
from django.contrib import messages
from dash.models import Payment
import pdb
from userprofile.models import Profiles
# Create your views here.


class MyCourses(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request):
        try:
            adimission = Profiles.objects.get(user=request.user)
        except:   adimission =  None
        front_end = Courses.objects.filter(material__name='Front-end-materials')
        my_back = Courses.objects.filter(material__name='Back-end-materials')
        return render(request, 'dashboard/training_materials.html',{'front_end':front_end, 'my_back':my_back,'adimission':adimission})
    
    
    def post(self,request):
        return render(request, 'dashboard/training_materials.html')


class Materialspayment(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        
        try:
            payments= Payment.objects.get(user=request.user)
        except:   payments =  None
        
        try:
            adimission = Profiles.objects.get(user=request.user)
        except:   adimission =  None
        
        return render(request, "dashboard/payment.html",{'payment':payments, 'adimission':adimission})
    
    def post(self, request):
        materials = request.POST['materials']
        amount_paid = request.POST['amount_paid']
        date  =      request.POST['date']
        payment_type = request.POST['payment_type']
        payment_file = request.FILES.get('myfiles')
        if not amount_paid :
            messages.error(request, 'fill all the form before submitting')
            return render(request, "dashboard/payment.html")
        
    
       
        mypayment = Payment.objects.create( user=request.user,amount=amount_paid,courses=materials, 
                   payment_type=payment_type, date=date,uplaod=payment_file)
        mypayment.mysave()
        
        mypayment.save()
        messages.success(request, 'payment for material submit successfully, refresh the page to generate payment reciept')
        return redirect('gen')
    

class Paymentslips(View):
    def get(self, request):
        try:
           
            payments= Payment.objects.get(user=request.user)
           
        except:   payments =  None
        return render(request, 'dashboard/slips.html',{'payment':payments})
    
    
    def post(self, request):
        return render(request, 'dashboard/slips.html')
    

class Gen(View):
    def get(self,request):
        return render(request, 'dashboard/gen.html')
    
    
    def post(self,request):
        return render(request, 'dashboard/gen.html')
        
        
            
       
   