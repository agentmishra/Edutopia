from django.urls import path
from . import views

# django.urls expects an app as an argument

urlpatterns=[
    path("",views.index),
    path("login/",views.login,name='login')
]