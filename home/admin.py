from django.contrib import admin
from home.models import Bloodbank, Hospital, Donor, Orders, Patient, Blood

# Register your models here.
admin.site.register(Bloodbank)
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(Orders)
admin.site.register(Patient)
admin.site.register(Blood)
