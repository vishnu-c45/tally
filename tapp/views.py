from pickle import FALSE
from django.contrib import messages

from .models import Employee,Create_employeegroup,Create_attendence, Rounding, compute_information, create_payhead,create_stockcate,create_stockgrp,create_stockitem,create_VoucherModels,create_goddown, gratuity,units,add_bank,E_found_trasfer
from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    return render(request,'base.html')

def stockgrp(request):
    std=create_stockgrp.objects.all()
    return render(request,'stockgroup.html',{'std':std}) 


def stockcate(request):
    std=create_stockcate.objects.all()
    return render(request,'stockcategory.html',{'std':std})    

def stockitem(request):
    pk=units.objects.all()
    sp=create_stockgrp.objects.all()
    return render(request,'stockitem.html',{'pk':pk ,'sp':sp})  

def stunits(request):
    ps=units()
    return render(request,'stunits.html',{'ps':ps}) 

def goddown(request):
    std=create_goddown.objects.all()
    return render(request,'goddown.html',{'std':std}) 

#payroll

def emp_grp(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employegroup.html',{'std':std})     

def employee(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employe.html',{'std':std})   

def payheads(request):
    std=Create_attendence.objects.all()
    return render(request,'payheads.html',{'std':std})   

def attendence(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence.html',{'std':std,'pk':pk})   

def salary(request):
    pk=create_payhead.objects.all()
    return render(request,'salary.html',{'pk':pk})   

def payhead2(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('salary')
    return render(request,'payhead_secondary.html')                   


def payvoucher(request):
    return render(request,'payroll.html')   

def group_secondary(request):
    std=create_stockgrp.objects.all()
    if request.method=='POST':
        lev=create_stockgrp()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.quntities_added=request.POST.get('qty')
        lev.save()
        return redirect('stockitem')

    return render(request,'group_secondary.html',{'std':std})    

def units_secondary(request):
    if request.method =='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')  
        std.save()
        return redirect('stockitem')

    return render(request,'units_secondary.html')

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
        #Bank
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
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
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
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
        period=request.POST['period']
        units1=request.POST['units']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
            period=period,
            units=units1,
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
        lev.maintain_Batches=request.POST.get('batches')
        lev.units=request.POST.get('units')
        lev.track_date_of_manufaturing=request.POST.get('Track')
        lev.use_expiry_dates=request.POST.get('Expiry')
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



def add_payhead(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads')

























             






        




