from django import forms
from django.forms import fields, widgets 
from .models import Patient, Bloodbank, Hospital, Donor, Blood

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient

        genderChoices = (
            ("M", "M"),
            ("F", "F"),
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
            'firstname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
            'lastname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"})
        }

class BloodbankForm(forms.ModelForm):
    class Meta:
        model = Bloodbank

        fields = "__all__"

        widgets = {
            'location': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
            'bankname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
        }

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital

        fields = "__all__"

        widgets = {
            'location': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
            'hospitalname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor

        fields = "__all__"

        genderChoices = (
            ("M", "M"),
            ("F", "F"),
        )

        widgets = {
            'gender': forms.Select(choices=genderChoices),
            'age': forms.NumberInput(attrs={'min':18,'max': '60','type': 'number'}),
            'firstname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
            'lastname': forms.TextInput(attrs={'pattern':"[A-Za-z]+"}),
            'phonenumber': forms.TextInput(attrs={'pattern':"[7-9]{1}[0-9]{9}"})
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


