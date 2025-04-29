from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register.html'),
    path('',views.home,name='home.html'),
    path('about',views.about,name='about.html'),
    path('services',views.services,name='services.html'),
    path('login',views.loginpage,name='login.html'),
    path('index',views.index,name='index.html'),
    path('public',views.public,name='public.html'),
    path('private',views.private,name='private.html'),
    path('privillage',views.privillage,name='privillage.html'),
    path('public_document',views.public_document,name='public_document.html'),
    path('private_document',views.private_document,name='private_document.html'),
    path('privillage_document',views.privillage_document,name='privillage_document.html'),
    path('your_document',views.your_document,name='your_document.html'),
    path('contact_us',views.contact_us,name='contact_us.html'),
    path('about_us',views.about_us,name='about_us.html'),
    path('enquiry', views.enquiry, name='enquiry.html'),
    path('feedback', views.feedback, name='feedback.html'),
    path('viewdata',views.viewdata),
    path('checklogin',views.checklogin),
    path('logout',views.logout),
    path('insertdocument',views.insertdocument),
    path('insertprivatedocument', views.insertprivatedocument),
    path('insertprivillagedocument', views.insertprivillagedocument),
    path('View_document', views.View_document),
    path('checkpassword', views.checkpass),
    path('password/<int:id>', views.password),
    path('enquirypage', views.enquirypage),
    path('addfeedback', views.addfeedback),
    path('verification',views.verification,name='verification.html')
]
