from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib  import messages
from django.http import JsonResponse
import json
from django.contrib import auth
from userprofile.models import Profiles
import pdb
import re
from django_ratelimit.decorators import ratelimit
from django.contrib.auth import authenticate, login, logout


User = get_user_model()

# Create your views here.

# class Usernamevalidation(View):
#     def post(self,request):
        #loading the html data and converting it to  python dic
        # data = json.loads(request.body)
        #pick the username from the data
        # username = data['username']
        # if not str(username).isalnum():
        #     return JsonResponse({'username_error': 'username should only contain alphameric character'})
        # return JsonResponse({'username_valid': 'yes'})


# Updated User validation Code by:Da'Guy
def uservalidation(request):
    username = request.GET.get('username', '').strip()  # Trim spaces

    if not username:  # Check if username is missing or empty
        return JsonResponse({'error': 'Username parameter is required'}, status=400)

    is_taken = User.objects.filter(username=username).exists()

    data = {
        'is_taken': is_taken,
        'message': "Username is already taken" if is_taken else "Username is available"
    }

    return JsonResponse(data)


# Old Phone verification Code

# def phonevalidation(request):
#     phone = request.GET.get('phone', None)
#     data = {
#         'is_taken': User.objects.filter(phone=phone).exists()
        
#     }
#     return JsonResponse(data)


# New Phone verification Code by:Da'Guy
def phonevalidation(request):
    phone = request.GET.get('phone', '').strip()  # Remove extra spaces

    if not phone:  # Handle missing or empty phone number
        return JsonResponse({'error': 'Phone number parameter is required'}, status=400)

    # if not re.fullmatch(r'^\+?\d{7,15}$', phone):  # Validate phone format
    #     return JsonResponse({'error': 'Invalid phone number format'}, status=400)

    is_taken = User.objects.filter(phone=phone).exists()

    data = {
        'is_taken': is_taken,
        'message': "Phone number is already registered" if is_taken else "Phone number is available"
    }

    return JsonResponse(data)





#  Old Email verification Code
# def emailvalidation(request):
#     email = request.GET.get('email')
#     data = {
#         'is_taken': User.objects.filter(email=email).exists()
        
#     }
#     return JsonResponse(data)
        

# New Email verification Code by:Da'Guy
# Added rate limiting to prevent abuse 
@ratelimit(key='ip', rate='5/m', method='GET', block=True)  # Limit to 5 requests per minute per IP
def emailvalidation(request):
    email = request.GET.get('email', '').strip()  # Remove extra spaces

    if not email:  # Handle missing or empty email
        return JsonResponse({'error': 'Email parameter is required'}, status=400)

    # Validate email format using regex
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.fullmatch(email_regex, email):
        return JsonResponse({'error': 'Invalid email format'}, status=400)

    is_taken = User.objects.filter(email=email).exists()

    data = {
        'is_taken': is_taken,
        'message': "Email is already registered" if is_taken else "Email is available"
    }

    return JsonResponse(data)

# New Phone verification Code by:Da'Guy
@ratelimit(key='ip', rate='5/m', method='GET', block=True)  # Limit to 5 requests per minute per IP
def phonevalidation(request):
    phone = request.GET.get('phone')
    data = {'is_taken': User.objects.filter(phone=phone).exists()}
    return JsonResponse(data)



# Old Registration Code
# class Registration(View):
#     def get(self, request):
#         return  render(request, 'register.html')
    
    
#     def post(self, request):
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         confirm_password = request.POST['password2']
#         username = request.POST['username']
        
#         if password !=confirm_password:
#             messages.error(request, "Password Not the same")
#             return  render(request, 'register.html')
#         if len(password)  < 5:
#             messages.error(request, "password too short try again")
#             return  render(request, 'register.html')
#         if User.objects.filter(phone=phone).exists():
#             messages.error(request,"phone number already been used ")
#             return  render(request, 'register.html')
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "email has been taken try again")
#             return  render(request, 'register.html')
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "username has been taken")
#             return  render(request, 'register.html')
        
#         user = User.objects.create_user(email=email, username=username, phone=phone)
        
#         data = {}
#         user.set_password(password)
        
#         if user.save():
#             data['status'] = 1
#             return JsonResponse(data)
       
        
#         # messages.success(request, "Account created successfully ")
        
            
           
        
#         # messages.success(request, "Account created successfully ")
        
#         return  render(request, 'register.html')
    
    

# Updated Registration Code by:Da'Guy
class Registration(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        username = request.POST['username']

        # Password validation
        if password != confirm_password:
            return JsonResponse({'status': 0, 'message': "Passwords do not match"}, status=400)
        if len(password) < 5:
            return JsonResponse({'status': 0, 'message': "Password too short"}, status=400)

        # Check if user already exists
        if User.objects.filter(phone=phone).exists():
            return JsonResponse({'status': 0, 'message': "Phone number already registered"}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 0, 'message': "Email already registered"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 0, 'message': "Username already taken"}, status=400)

        # Create user
        user = User.objects.create_user(email=email, username=username, phone=phone)
        user.set_password(password)
        user.save()

        return JsonResponse({'status': 1, 'message': "Account created successfully"})


# Old Login Code
# class Login(View):
#     def get(self, request):
#         return  render(request, 'registration/login.html')
    
#     def post(self, request):
#         phone = request.POST['phone']
#         password = request.POST['password']
       
#         # ison =  Profiles.objects.filter(user=request.user).exists()
        
        
#         if not User.objects.filter(phone=phone).exists():
#             messages.error(request, 'your phone number is invalid')
#             return  render(request, 'registration/login.html')
#         if password and phone:
#             user = auth.authenticate(phone=phone, password=password)
            
#             if user:
#                 auth.login(request,user)
#                 # if not ison:
#                 #     return redirect('profile')
            
               
#                 return redirect('dash')
                
            
#             messages.error(request, 'incorrect password try again')
#             return  render(request, 'registration/login.html')
        
     
#         messages.error(request, "empty field not allowed")
#         return  render(request, 'registration/login.html')
        
        # return  render(request, 'login.html')



# Updated Login Code by:Da'Guy
class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']

        if not User.objects.filter(phone=phone).exists():
            return JsonResponse({'status': 0, 'message': "Invalid phone number"}, status=400)

        user = auth.authenticate(phone=phone, password=password)
        if user:
            auth.login(request, user)
            # return JsonResponse({"redirect_url": "/dashboard/"})
            return redirect('dash')

        return redirect("login")


class Logout(View):
    def get(self,request):
        auth.logout(request)
        messages.success(request,'logout successfully')
        return redirect('login')