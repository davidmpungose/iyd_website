from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('services/',views.services, name='services'),
    path('contact-us/',views.contact_us, name='contact-us'),
    path('about-us/',views.about_us , name='about-us'),
    path('guide/',views.guide, name='guide')
]

