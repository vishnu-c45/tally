from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stgrp',views.stockgrp,name='stockgrp'),
    path('stcate',views.stockcate,name='stockcate'),
    path('stitem',views.stockitem,name='stockitem'),
    path('stunits',views.stunits,name='stunits'),
    path('goddown',views.goddown,name='goddown'),
    path('empgroup',views.emp_grp,name='emp_grp'),
    path('employee',views.employee,name='employee'),
    path('payheads',views.payheads,name='payheads'),
    path('attendence',views.attendence,name='attendence'),
    path('payvoucher',views.payvoucher,name='payvoucher'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('addemp_grp',views.addemp_group,name='addemp_group'),
    path('emp_attendence',views.emp_attendence,name='emp_attendence'),
    path('add_stockcate',views.add_stockcate,name='add_stockcate'),
    path('stockgrp',views.add_stockgrp,name='add_stockgrp'),
    path('add_units',views.add_units,name='add_units'),
    path('add_stockitem',views.add_stockitem,name='add_stockitem'),
    path('voucher',views.add_voucher,name='add_voucher'),
    path('add_goddown',views.add_goddown,name='add_goddown'),
    path('add_pay_head',views.add_payhead,name='add_payhead'),
    path('units2',views.units_secondary,name='units_secondary'),
    path('group2',views.group_secondary,name='group_secondary'),
    path('salary',views.salary1,name='salary1'),
    path('payhead2',views.payhead2,name='payhead2'),
    path('sal/<int:pk>',views.salary_sec,name="salary_sec"),
    path('load',views.load,name='load'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    #secondary
    path('group3',views.group_secondary2,name='group_secondary2'),
    path('add_stockcate2',views.add_stockcate2,name='add_stockcate2'),
    path('add_goddown2',views.add_goddown2,name='add_goddown2'),
    path('empgroup2',views.emp_grp2,name='emp_grp2'),
    path('attendence2',views.attendence2,name='attendence2'),
     path('addemp_grp2',views.addemp_group2,name='addemp_group2'),
]