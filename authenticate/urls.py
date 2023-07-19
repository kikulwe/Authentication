from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.home, name='hello i am home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),   
]
