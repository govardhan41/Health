from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=100)
    purpose = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date} with Dr. {self.doctor}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    diagnosis = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date}: {self.diagnosis}"


class Doctor