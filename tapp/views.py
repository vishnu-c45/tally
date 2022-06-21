from re import A
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def stockgrp(request):
    return render(request,'stockgroup.html') 


def stockcate(request):
    return render(request,'stockcategory.html')        
