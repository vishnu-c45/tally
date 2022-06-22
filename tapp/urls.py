from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stgrp',views.stockgrp,name='stockgrp'),
    path('stcate',views.stockcate,name='stockcate'),
    path('stitem',views.stockitem,name='stockitem'),
    path('stunits',views.stunits,name='stunits'),
    path('goddown',views.goddown,name='goddown')
    
]