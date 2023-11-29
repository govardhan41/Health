from django.urls import path
from .views import patient_list, appointment_list, medical_record_list

urlpatterns = [
    path('patients/', patient_list, name='patient_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('medical_records/', medical_record_list, name='medical_record_list'),
]
