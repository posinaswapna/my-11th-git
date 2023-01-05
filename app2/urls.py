from django.urls import path
from app2.views import *
app_name='pavan'
urlpatterns=[
    path('swap/',swap,name='swap'),
]