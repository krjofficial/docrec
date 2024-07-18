from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient

# Create your views here.

def base(request):

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    return render(request, 'base.html', {'doctors':doctors, 'patients': patients})


def doctor_details(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)
    
    return render(request, 'doctor_details.html', {'doctor': doctor})
    

def book_appointment(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.visit_count += 1
    doctor.save()
    return redirect('base')



# doctor name - clickable redirect doctor details page
# doctor details - name, id, longitude, latitude, visit count, button - book appointment
# book appointment - increment the visit count by 1 and redirect home
