from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage, Appointment

admin.site.register(ContactMessage)
admin.site.register(Appointment)