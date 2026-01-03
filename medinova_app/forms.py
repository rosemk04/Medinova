from django import forms
from .models import ContactMessage, Appointment, Blogs
from .models import Doctor, Testimonial

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"

