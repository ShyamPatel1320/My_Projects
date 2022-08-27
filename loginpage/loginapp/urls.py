from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginhome,name="login"),
    path('login.html',views.loginhome,name="login"),
    path('signup.html',views.signuphome,name="signup"),
    path('forgot.html',views.forgothome,name="forgot"),
    path('resetpassword.html',views.resethome,name="reset"),
    path('otp.html',views.otphome,name="otp"),
    path('web.html',views.webhome,name="web"),
    path('acccreated.html',views.acccreated,name="acccreated"),
    path('updatepass.html',views.updatepasshome,name="updatepass"),
]