from django.contrib import admin  
from django.urls import path  
from . import views 

urlpatterns = [ 
path('',views.show),   
path('add', views.add),  
path('show', views.show), 
path('vaccine/<int:id>', views.vacshow), 
path('edit/<int:id>', views.edit),  
path('update/<int:id>', views.update),  
path('delete/<int:id>', views.destroy), 
path('addVac/<int:id>',views.vacadd),
path('addVac',views.vacadd),
] 