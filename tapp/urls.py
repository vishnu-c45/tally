from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stockgrp',views.stockgrp,name='stockgrp'),
    path('stockcate',views.stockcate,name='stockcate'),
    
]