from django import forms
from django.forms import fields, widgets 
from .models import Patient, Bloodbank, Hospital, Donor, Blood

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient

        genderChoices = (
            ("Male", "M"),
            ("Female", "F"),
        )

        bloodgroupChoices = (
            ("O+", "O+" ),
            ("O-", "O-" ),
            ("A+", "A+" ),
            ("A-", "A-" ),
            ("B+", "B+" ),
            ("B-", "B-" ),
            ("AB+", "AB+" ),
            ("AB-", "AB-" ),
        )

        fields = "__all__"
        widgets = {
            'gender': forms.Select(choices=genderChoices),
            'pbloodtype': forms.Select(choices=bloodgroupChoices),
        }

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

        genderChoices = (
            ("Male", "M"),
            ("Female", "F"),
        )

        widgets = {
            'gender': forms.Select(choices=genderChoices),
            'age': forms.NumberInput(attrs={'min':18,'max': '60','type': 'number'})
        }


class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood

        fields = "__all__"

        bloodgroupChoices = (
            ("O+", "O+" ),
            ("O-", "O-" ),
            ("A+", "A+" ),
            ("A-", "A-" ),
            ("B+", "B+" ),
            ("B-", "B-" ),
            ("AB+", "AB+" ),
            ("AB-", "AB-" ),
        )

        widgets = {
            'bloodtype': forms.Select(choices=bloodgroupChoices)
        }


