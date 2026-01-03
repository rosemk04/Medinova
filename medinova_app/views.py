from django.shortcuts import render, redirect ,get_object_or_404  
from .forms import ContactForm , AppointmentForm
from .forms import BlogForm, TestimonialForm
from django.contrib import messages
from .models import Blogs, Testimonial
from .models import Doctor  
from .forms import DoctorForm 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blogs.objects.all().order_by('-published_at')
    return render(request, 'blog.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, 'detail.html', {'blog': blog})

def price(request):
    return render(request, 'price.html')

def search(request):
    return render(request, 'search.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'testimonial.html', {'testimonials': testimonials})


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





@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, Admin!")
            return redirect('admin_dashboard')
        else:   
            messages.error(request, "There was an error logging in, try again.")
            return redirect('user_login')
    return render(request, 'admin_pages/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('user_login')

@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request, 'admin_pages/dashboard.html')

@login_required(login_url='user_login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog added successfully!')
            return redirect('view_blogs')
    else:
        form = BlogForm()
    return render(request, 'admin_pages/add_blog.html')


@login_required(login_url='user_login')
def view_blogs(request):
    blogs = Blogs.objects.all().order_by('-published_at')
    return render(request, 'admin_pages/view_blogs.html', {'blogs': blogs})

@login_required(login_url='user_login')
def update_blog(request, id):
    blog = get_object_or_404(Blogs, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('view_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin_pages/update_blog.html', {'blog': blog, 'form': form})

@login_required(login_url='user_login')
def delete_blog(request, id):
    blog = get_object_or_404(Blogs, id=id)
    blog.delete()
    return redirect('view_blogs')
    return render(request, 'admin_pages/delete_blog.html', {'blog': blog})

@login_required(login_url='user_login')
def view_appointments(request):
    return render(request, 'admin_pages/view_appointments.html')

@login_required(login_url='user_login')
def add_testimony(request):
    return render(request, 'admin_pages/add_testimony.html')


@login_required(login_url='user_login')
def view_testimony(request):
    return render(request, 'admin_pages/view_testimony.html')

@login_required(login_url='user_login')
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_doctors')
    else:
        form = DoctorForm()
    return render(request, 'admin_pages/add_doctor.html', {'form': form})

@login_required(login_url='user_login')
def view_doctors(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the DB
    return render(request, 'admin_pages/view_doctors.html', {'doctors': doctors})

@login_required(login_url='user_login')
def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('view_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'admin_pages/update_doctor.html', {'doctor': doctor, 'form': form})

@login_required(login_url='user_login')
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('view_doctors')


@login_required(login_url='user_login')
def add_testimony(request):
    if request.method == 'POST':
        
        form = TestimonialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_testimony')
    else:
        form = TestimonialForm()

    return render(request, 'admin_pages/add_testimony.html', {
        'form': form
    })


@login_required(login_url='user_login')
def view_testimony(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'admin_pages/view_testimony.html', {
        'testimonials': testimonials
    })


@login_required(login_url='user_login')
def edit_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)

    if request.method == 'POST':
        # 🔴 REQUIRED for image update
        form = TestimonialForm(
            request.POST,
            request.FILES,
            instance=testimonial
        )

        if form.is_valid():
            form.save()
            return redirect('view_testimony')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'admin_pages/edit_testimonial.html', {
        'form': form,
        'testimonial': testimonial
    })


@login_required(login_url='user_login')
def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    testimonial.delete()
    return redirect('view_testimony')
