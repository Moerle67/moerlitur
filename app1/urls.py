from django.urls import path 
from . import views 

urlpatterns = [ 
    path('' , views.index, name='index'),
    path('tools' , views.tools, name='tools'),
]