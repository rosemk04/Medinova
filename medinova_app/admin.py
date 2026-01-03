from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage, Appointment, Blogs
from .models import Doctor, Testimonial

admin.site.register(ContactMessage)
admin.site.register(Appointment)
admin.site.register(Blogs)
admin.site.register(Doctor)
admin.site.register(Testimonial)
