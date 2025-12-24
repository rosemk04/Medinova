from django import forms
from .models import ContactMessage, Appointment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
