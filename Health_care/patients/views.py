from django.shortcuts import render
from .models import Patient, Appointment, MedicalRecord

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'patients/appointment_list.html', {'appointments': appointments})

def medical_record_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'patients/medical_record_list.html', {'medical_records': medical_records})
