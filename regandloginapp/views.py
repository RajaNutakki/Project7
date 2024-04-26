from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,template_name='home.html')
class RegisterInput(View):
    def get(self,request):
        return render(request,template_name='register.html')
class Register(View):
    def post(self,request):
        r1=Reg(fname=request.POST["firstname"],
               lname=request.POST["lastname"],
               email=request.POST["email"],
               mobile=request.POST["mobile"],
               dob=request.POST["dob"],
               username=request.POST["username"],
               password=request.POST["password"],
               cpassword=request.POST["cpassword"])
        r1.save()
        return HttpResponse('your Successfully registered')
class LoginInput(View):
    def get(self,request):
        return render(request,template_name='login.html')
class Login(View):
    def post(self,request):
        qs=Reg.objects.filter(username=request.POST["username"],
                              password=request.POST["password"])
        if qs:
            return HttpResponse("login successful")
        else:
            return HttpResponse("Login failed")
