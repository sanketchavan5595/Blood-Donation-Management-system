# from django.http.response import HttpResponse
from django.db.models.query import RawQuerySet
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from home.models import Bloodbank, Donor, Hospital, Patient, Blood, Orders
from home.forms import PatientForm, BloodbankForm, HospitalForm, DonorForm, BloodForm
# import mysql.connector

# conn = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '7387479297',
#     database = 'dbmsminiproject'
# )

# Create your views here.
def index(request):
    # return HttpResponse('this is homepage')
    return render(request=request, template_name='index.html')

# bloodbank operations
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

def updateBloodbank(request, pk):
    b = Bloodbank.objects.get(bankid = pk)
    form = BloodbankForm(instance=b)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = BloodbankForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/bloodbank')

    return render(request=request, template_name='updateBloodbank.html', context=context)

def deleteBloodbank(request, pk):
    p = Bloodbank.objects.get(bankid = pk)
    if request.method == "POST":
        p.delete()
        return redirect('/bloodbank')

    context = {'item': p}
    return render(request=request, template_name='deleteBloodbank.html', context=context)

        
# hospital operations 
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

def updateHospital(request, pk):
    b = Hospital.objects.get(hospitalid = pk)
    form = HospitalForm(instance=b)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/hospital')

    return render(request=request, template_name='updateHospital.html', context=context)

def deleteHospital(request, pk):
    p = Hospital.objects.get(hospitalid = pk)
    if request.method == "POST":
        p.delete()
        return redirect('/hospital')

    context = {'item': p}
    return render(request=request, template_name='deleteHospital.html', context=context)


# donor operations 
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

def updateDonor(request, pk):
    b = Donor.objects.get(donorid = pk)
    form = DonorForm(instance=b)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/donor')

    return render(request=request, template_name='updateDonor.html', context=context)

def deleteDonor(request, pk):
    p = Donor.objects.get(donorid = pk)
    if request.method == "POST":
        p.delete()
        return redirect('/donor')

    context = {'item': p}
    return render(request=request, template_name='deleteDonor.html', context=context)


# Blood operations 
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

def updateBlood(request, pk):
    b = Blood.objects.get(bloodid = pk)
    form = BloodForm(instance=b)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = BloodForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/blood')

    return render(request=request, template_name='updateBlood.html', context=context)

def deleteBlood(request, pk):
    p = Blood.objects.get(bloodid = pk)
    if request.method == "POST":
        p.delete()
        return redirect('/blood')

    context = {'item': p}
    return render(request=request, template_name='deleteBlood.html', context=context)


# Patient Operations 
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

def updatePatient(request, pk):
    p = Patient.objects.get(patientid = pk)
    form = PatientForm(instance=p)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/patient')

    return render(request=request, template_name='updatePatient.html', context=context)

def deletePatient(request, pk):
    p = Patient.objects.get(patientid = pk)
    if request.method == "POST":
        p.delete()
        return redirect('/patient')

    context = {'item': p}
    return render(request=request, template_name='deletePatient.html', context=context)
