from django.contrib import messages

from .models import Employee,Create_employeegroup,Create_attendence,create_stockcate,create_stockgrp,create_stockitem,create_VoucherModels,create_goddown,units
from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    return render(request,'base.html')

def stockgrp(request):
    std=create_stockgrp.objects.all()
    return render(request,'stockgroup.html',{'std':std}) 


def stockcate(request):
    return render(request,'stockcategory.html',)    

def stockitem(request):
    sp=create_stockgrp.objects.all()
    std=create_stockcate.objects.all()
    pk=units.objects.all()
    return render(request,'stockitem.html',{'std':std,'pk':pk,'sp':sp})  

def stunits(request):
    ps=units()
    return render(request,'stunits.html',{'ps':ps}) 

def goddown(request):
    std=create_goddown.objects.all()
    return render(request,'goddown.html',{'std':std}) 

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
       
        return render(request,'employe.html')


def addemp_group(request):
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
        messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')



def emp_attendence(request):
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('attendence')



def add_stockcate(request):
    if request.method=='POST':
        name=request.POST['name']  
        alias=request.POST['alias']
        under=request.POST['under']
        std=create_stockcate(name=name,
                        alias=alias,
                        under=under,
                        )  

        std.save()     
        return redirect('stockcate')  
        # return render(request,'stockcategory.html')         

def add_stockgrp(request):
    if request.method=='POST':
        lev=create_stockgrp()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.quntities_added=request.POST.get('qty')
        lev.save()
        return redirect('stockgrp')


def add_units(request):
    if request.method=='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')  
        std.save()
        return redirect('stunits')

def add_stockitem(request):
     if request.method=='POST':
        lev=create_stockitem()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.category=request.POST.get('cat')
        lev.units=request.POST.get('units')
        lev.rate_of_duty=request.POST.get('rate')
        lev.save()
        return redirect('stockitem')



def add_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        use_effct_date = request.POST['effect']  
        allow_zero_trans = request.POST['trans']  
        allow_naration_in_vou = request.POST['narr']  
        optional = request.POST['optical'] 
        provide_narr = request.POST['ledg']  
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        std.save()
        return redirect('payvoucher')

    return render(request, 'payroll.html')     

def add_goddown(request):
    if request.method =='POST':
        lev=create_goddown()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.save()
        return redirect('goddown')
    return render(request,'goddown.html')    



             






        




