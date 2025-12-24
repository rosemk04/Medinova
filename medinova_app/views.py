from django.shortcuts import render, redirect   
from .forms import ContactForm , AppointmentForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def detail(request):
    return render(request, 'detail.html')
def price(request):
    return render(request, 'price.html')
def search(request):
    return render(request, 'search.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # reload after submit
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment')  # reload after submit
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})