# from django.http.response import HttpResponse
from django.db.models.query import RawQuerySet
from django.shortcuts import render, HttpResponse
from home.models import Bloodbank, Donor, Hospital, Patient, Blood, Orders
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7387479297',
    database = 'dbmsminiproject'
)

# Create your views here.
def index(request):
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='index.html')

def bloodbank(request):
    bloodbank = Bloodbank.objects.all()
    context = {
        'rows': bloodbank
    }
    if request.method == 'POST':
        bName = request.POST.get('bankName')
        location = request.POST.get('location')
        bank = Bloodbank(bankname = bName, location = location)
        bank.save()
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='bloodbank.html', context=context)


        

def hospital(request):
    hospital = Hospital.objects.all()
    context = {
        'hospital': hospital
    }
    if request.method == 'POST':
        hName = request.POST.get('hospitalName')
        location = request.POST.get('location')
        h = Hospital(hospitalname = hName, location = location)
        h.save()
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='hospital.html', context=context)


def donor(request):
    donor = Donor.objects.all()
    context = {
        'donor': donor,
        'max_id': len(Bloodbank.objects.all())
    }

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phonenumber = request.POST.get('phonenumber')
        bankid = Bloodbank.objects.get(bankid = request.POST.get('bankid'))
        # bankid = request.POST.get('bankid')
        d = Donor(firstname = firstname, lastname = lastname, gender = gender, age = age, phonenumber = phonenumber, bankid = bankid)
        d.save()
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='donor.html', context=context)


def blood(request):
    blood = Blood.objects.all()
    context = {
        'blood': blood,
        'maxBankCount': len(Bloodbank.objects.all()),
        'maxDonorCount': len(Donor.objects.all())
    }

    if request.method == 'POST':
        bloodtype = request.POST.get('bloodtype')
        bankid = Bloodbank.objects.get(bankid = request.POST.get('bankid'))
        donorid = Donor.objects.get(donorid = request.POST.get('donorid'))
        b = Blood(bloodtype = bloodtype, bankid = bankid, donorid = donorid)
        b.save()

    return render(request=request, template_name='blood.html', context=context)

def patient(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient,
        'maxHospitalCount': len(Hospital.objects.all())
    }

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        pbloodtype = request.POST.get('pbloodtype')
        hospitalid = Hospital.objects.get(hospitalid = request.POST.get('hospitalid'))
        p = Patient(firstname = firstname, lastname = lastname, age = age, gender = gender, pbloodtype = pbloodtype, hospitalid = hospitalid)
        p.save()
    return render(request=request, template_name='patient.html', context=context)

def mysqltrial(request):
    cursor = conn.cursor()
    sql = 'select * from bloodbank'
    cursor.execute(sql)
    rows = cursor.fetchall()
    context = {
        'rows': rows
    }

    return render(request=request, template_name='mysqltrial.html', context=context)
