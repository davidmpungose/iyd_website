from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .form import ContactForm
from .models import ContactUs
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def guide(request):
    return render(request, 'theming-kit.html')

def about_us(request):
    return render(request, 'core/about-us.html')

def services(request):
    return render(request, 'core/services.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # Check if form is valid
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message'] 
            subject = f"{first_name} Email Inquiry."

            # Your data processing goes here (e.g., print, email)
            print(f"First Name: {first_name}")  # Print data
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ["inhlosoyetfu@gmail.com"],
                )
                messages.info(request, "Your email has been sent.")
            except Exception as e:
                print(f"Error sending email: {e}")  # Print error message for debugging
                messages.error(request, "Something went wrong. Please try again later.")
            messages.info(request, "Your email has been sent.")
            return redirect('contact-us')

        else:
            message.error(request, "Something went wrong.")

    
    return render(request, 'core/contact-us.html', {})