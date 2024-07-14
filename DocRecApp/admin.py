from django.contrib import admin
from models import Location, Doctor, Patient, Visit

# Register your models here.
admin.site.register(Location)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Visit)

