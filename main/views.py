
from ctypes.wintypes import SERVICE_STATUS_HANDLE
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from flask import flash
from main.models import *
from django.core.files.storage import FileSystemStorage
import datetime
import django.utils
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum,Count

def index(request):
    view=profile.objects.all()

   

    if "login" in request.POST:
        uname=request.POST['uname']
        password=request.POST['pass']
        print(uname)
        try:
            print("###############################")
            lg=login.objects.get(username=uname,password=password)
            print(lg)
            request.session['login_id']=lg.pk
            if lg.usertype == 'admin':
                # return HttpResponse("<script>alert('Login Success');window.location='/adminhome'</script>")
                return render(request,'toaster.html',{'message':'Login Successfull','location': '/adminhome'})
            elif lg.usertype == 'user':
                print("*******************************")
                uu=user.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['username']=uu.fname+" "+uu.lname
                request.session['user_id']=uu.pk
                
                return render(request,'toaster.html',{'message':'Login Successfull','location': 'userhome'})
        except: 
            return render(request,'toaster.html',{'message':'Invalid Username Or Password','location': '/'})
            # return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/'</script>")
    
    if "register" in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pass']
       
        lg=login(username=username,password=password,usertype='pending')
        lg.save()
        
        user_reg1=user(fname=fname,lname=lname,place=place,phone=phone,email=email,logins=lg)
        user_reg1.save()
        
        
        subject = 'Confirmation Link'
        message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{lg.login_id}>verify</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        
        # return HttpResponse("<script>alert('Successfully Added');window.location='/'</script>")
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/'})

   


    return render(request,'public_section.html',{'view':view,})



def login_page(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        print(uname)
        try:
            print("###############################")
            lg=login.objects.get(username=uname,password=password)
            print(lg)
            request.session['login_id']=lg.pk
            if lg.usertype == 'admin':
                return HttpResponse("<script>alert('Login Success');window.location='/adminhome'</script>")
            
            elif lg.usertype == 'user':
                print("*******************************")
                uu=user.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['user_id']=uu.pk
                
                return HttpResponse("<script>alert('Login Success');window.location='/userhome'</script>")
        except:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/login'</script>")
        
    return render(request,'login.html')

def user_reg(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pass']
       
        lg=login(username=username,password=password,usertype='pending')
        lg.save()
        
        user_reg1=user(fname=fname,lname=lname,place=place,phone=phone,email=email,logins=lg)
        user_reg1.save()
        
        
        
        return HttpResponse("<script>alert('Successfully Added');window.location='/login'</script>")

    return render(request,'user_registration.html')


def acceptcustomer_username(request,id):
    cus=login.objects.get(login_id=id)
    cus.usertype='user'
    cus.save()
    # return HttpResponse("<script>alert('Verified');window.location='/'</script>")
    return render(request,'toaster.html',{'message':'Verified','location': '/'})


# Create your views here.
