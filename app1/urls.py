from django.urls import path
from app1.views import *
app_name='swapna'
urlpatterns=[
    path('p1/',p1,name='p1'),
]