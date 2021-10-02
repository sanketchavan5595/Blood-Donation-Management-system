from django import forms
from django.forms import fields 
from .models import Patient, Bloodbank, Hospital, Donor, Blood

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient

        fields = "__all__"

class BloodbankForm(forms.ModelForm):
    class Meta:
        model = Bloodbank

        fields = "__all__"

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital

        fields = "__all__"

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor

        fields = "__all__"

class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood

        fields = "__all__"
