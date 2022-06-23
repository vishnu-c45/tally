from re import A
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'base.html')

def stockgrp(request):
    return render(request,'stockgroup.html') 


def stockcate(request):
    return render(request,'stockcategory.html')    

def stockitem(request):
    return render(request,'stockitem.html')  

def stunits(request):
    return render(request,'stunits.html') 

def goddown(request):
    return render(request,'goddown.html') 

#payroll

def emp_grp(request):
    return render(request,'employegroup.html')     

def employee(request):
    return render(request,'employe.html')               

