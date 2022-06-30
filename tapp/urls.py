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
    
]