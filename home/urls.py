from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('bloodbank', views.bloodbank, name='bloodbank'),
    path('hospital', views.hospital, name='hospital'),
    path('donor', views.donor, name='donor'),
    path('blood', views.blood, name='blood'),
    path('patient', views.patient, name='patient'),
    path('mysqltrial', views.mysqltrial, name='mysqltrial'),

]