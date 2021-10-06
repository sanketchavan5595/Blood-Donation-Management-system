from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),

    path('bloodbank', views.bloodbank, name='bloodbank'),
    path('updateBloodbank/<int:pk>/', views.updateBloodbank, name='updateBloodbank'),
    path('deleteBloodbank/<int:pk>/', views.deleteBloodbank, name='deleteBloodbank'),


    path('hospital', views.hospital, name='hospital'),
    path('updateHospital/<int:pk>/', views.updateHospital, name='updateHospital'),
    path('deleteHospital/<int:pk>/', views.deleteHospital, name='deleteHospital'),

    path('donor', views.donor, name='donor'),
    path('updateDonor/<int:pk>/', views.updateDonor, name='updateDonor'),
    path('deleteDonor/<int:pk>/', views.deleteDonor, name='deleteDonor'),


    path('blood', views.blood, name='blood'),
    path('updateBlood/<int:pk>/', views.updateBlood, name='updateBlood'),
    path('deleteBlood/<int:pk>/', views.deleteBlood, name='deleteBlood'),

    path('patient', views.patient, name='patient'),
    path('updatePatient/<int:pk>/', views.updatePatient, name='updatePatient'),
    path('deletePatient/<int:pk>/', views.deletePatient, name='deletePatient'),
    
    
]