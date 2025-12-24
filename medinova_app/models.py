from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


import datetime

class Appointment(models.Model):
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=150)
    patient_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor} ({self.date})"
