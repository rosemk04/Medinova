from django.urls import path
from .import views
urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('appointment/',views.appointment,name='appointment'),
    path('blog/',views.blog,name='blog'),
    path('blog/<int:id>/', views.detail, name='detail'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('price/',views.price,name='price'),
    path('search/',views.search,name='search'),
    path('service/',views.service,name='service'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),


   
    path('login/', views.user_login, name='user_login'),
    path('logout-user/', views.logout_user, name='logout_user'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('view_blogs/', views.view_blogs, name='view_blogs'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_doctors/', views.view_doctors, name='view_doctors'),
    path('update_doctor/<int:id>/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('add_testimony/', views.add_testimony, name='add_testimony'),
    path('view_testimony/', views.view_testimony, name='view_testimony'),
    path('edit-testimonial/<int:id>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete-testimonial/<int:id>/', views.delete_testimonial, name='delete_testimonial'),


    
]