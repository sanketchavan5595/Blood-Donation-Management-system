# from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Bloodbank, Donor, Hospital, Patient, Blood, Orders

# Create your views here.
def index(request):
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='index.html')

def bloodbank(request):
    bloodbank = Bloodbank.objects.all()
    context = {
        'bloodbank': bloodbank
    }
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='bloodbank.html', context=context)


def hospital(request):
    hospital = Hospital.objects.all()
    context = {
        'hospital': hospital
    }
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='hospital.html', context=context)


def donor(request):
    donor = Donor.objects.all()
    context = {
        'donor': donor
    }
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='donor.html', context=context)


def blood(request):
    bloodbank = Blood.objects.all()
    context = {
        'blood': blood
    }
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='blood.html', context=context)

def patient(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient
    }
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='patient.html', context=context)



