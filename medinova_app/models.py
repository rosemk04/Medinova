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


class Blogs(models.Model):
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=300)
    bio = models.TextField(blank=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    patient_name = models.CharField(max_length=300)
    profession = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

