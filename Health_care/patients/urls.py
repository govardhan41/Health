# patients/urls.py

# from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
    path('patientlist/',views.patient_list,name='patient-list'),
    path('apointmentslist/',views.appointment_list),
    path('medicalrecordslist/',views.medical_record_list),
]