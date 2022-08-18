from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('profit',views.profit,name='profit'),
    path('stockcate',views.stockcate,name='stockcate'),
    
]