from ctypes.wintypes import SERVICE_STATUS_HANDLE
from django.db import models

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)


class profile(models.Model):
    profile_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=225)
    details=models.CharField(max_length=225)
    since=models.CharField(max_length=225)
    licence=models.CharField(max_length=225)


class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.EmailField()
    logins=models.ForeignKey(login,on_delete=models.CASCADE)




