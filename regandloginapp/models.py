from django.db import models
class Reg(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    mobile=models.CharField(max_length=13)
    dob=models.CharField(max_length=20)
    username=models.CharField(max_length=10, primary_key=True)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
