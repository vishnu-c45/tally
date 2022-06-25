from .models import Employee
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

def payheads(request):
    return render(request,'payheads.html')   

def attendence(request):
    return render(request,'attendence.html')                 


def payvoucher(request):
    return render(request,'payroll.html')   

def addemployee(request):
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['under']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        
        std = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,


        )

        std.save()
        return render(request,'load_create_employee.html')




