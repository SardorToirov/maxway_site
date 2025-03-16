from django.urls import path
from .views import *

urlpatterns =[
    path('',home_max_way,name='home_page'),
    path('order/',main_order,name='main_order')
]