from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib  import messages
from django.http import JsonResponse
import json
from django.contrib import auth
from userprofile.models import Profiles
import pdb


User = get_user_model()










# Create your views here.


# class Usernamevalidation(View):
#     def post(self,request):
        #loading the html data and converting it to  python dic
        # data = json.loads(request.body)
        #pick the username from the data
        # username = data['username']
        # if not str(username).isalnum():
        #     return JsonResponse({'username_error': 'username should only contain alphameric charater'})
        # return JsonResponse({'username_valid': 'yes'})


def uservalidation(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
        
    }
    
    # if data['is_taken']:
    #     data['error_message'] = ''
    return JsonResponse(data)


def phonevalidation(request):
    phone = request.GET.get('phone', None)
    data = {
        'is_taken': User.objects.filter(phone=phone).exists()
        
    }
    return JsonResponse(data)







def emailvalidation(request):
    email = request.GET.get('email')
    data = {
        'is_taken': User.objects.filter(email=email).exists()
        
    }
    return JsonResponse(data)
        




class Registration(View):
    def get(self, request):
        return  render(request, 'register.html')
    
    
    def post(self, request):
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        comfirm_password = request.POST['password2']
        username = request.POST['username']
        
        if password !=comfirm_password:
            messages.error(request, "Password Not the same")
            return  render(request, 'register.html')
        if len(password)  < 5:
            messages.error(request, "password too short try again")
            return  render(request, 'register.html')
        if User.objects.filter(phone=phone).exists():
            messages.error(request,"phone number already been used ")
            return  render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email has been taken try again")
            return  render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "username has been taken")
            return  render(request, 'register.html')
        user = User.objects.create_user(email=email, username=username, phone=phone)
        
        data = {}
        user.set_password(password)
        
        if user.save():
            data['status'] = 1
            return JsonResponse(data)
       
        
        # messages.success(request, "Account created successfully ")
        
            
           
        
        # messages.success(request, "Account created successfully ")
        
        return  render(request, 'register.html')
    
    
class Login(View):
    def get(self, request):
        return  render(request, 'registration/login.html')
    
    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
       
        # ison =  Profiles.objects.filter(user=request.user).exists()
        
        
        if not User.objects.filter(phone=phone).exists():
            messages.error(request, 'your phone number is invalid')
            return  render(request, 'login.html')
        if password and phone:
            user = auth.authenticate(phone=phone, password=password)
            
            if user:
                auth.login(request,user)
                # if not ison:
                #     return redirect('profile')
            
               
                return redirect('dash')
                
            
            messages.error(request, 'incorrect password try again')
            return  render(request, 'registration/login.html')
        
     
        messages.error(request, "empty field not allowed")
        return  render(request, 'registration/login.html')
        
        # return  render(request, 'login.html')
    
     
class Logout(View):
    def get(self,request):
        auth.logout(request)
        messages.success(request,'logout sucessfully')
        return redirect('login')
            
        
        
    
    