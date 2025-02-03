from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .form import ContactForm
from .models import ContactUs
from django.contrib.auth import authenticate, login, logout
from blog.form import TenantRegistrationForm
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Sorry. Something went wrong.')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
    
def register_user(request):
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account created. Please log in.')
            return redirect('login')
        else:
            messages.warning(request, 'Sorry. Something went wrong.')
            print(form.errors)
            context = {'form': form}
            return render(request, 'registration/register.html', context)
    else:
        form = TenantRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

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
    # Replace with your actual FormSubmit URL
    formsubmit_url = "https://formsubmit.co/inhlosoyetfu@gmail.com"

    if request.method == 'POST':
        # No form validation needed as FormSubmit handles it
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        from_email = request.POST['email']
        message = request.POST['message']
        subject = f"{first_name} Email Inquiry."

        # Prepare data for FormSubmit
        form_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": from_email,
            "message": message,
        }

        try:
            # Send POST request to FormSubmit using requests library (assuming installed)
            import requests
            response = requests.post(formsubmit_url, data=form_data)
            response.raise_for_status()  # Raise exception for non-200 status codes

            messages.info(request, "Your email has been sent.")
        except requests.exceptions.RequestException as e:
            print(f"Error sending to FormSubmit: {e}")
            messages.error(request, "Something went wrong. Please try again later.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, "Something went wrong. Please try again later.")

        return redirect('contact-us')

    return render(request, 'core/contact-us.html', {})


def contact_us(request):
     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():  # Check if form is valid
             first_name = form.cleaned_data['first_name']
             last_name = form.cleaned_data['last_name']
             from_email = form.cleaned_data['email']
             message = form.cleaned_data['message'] 
             subject = f"{first_name} Email Inquiry."

             #email body to be received
             email_body = f"""
                First Name: {first_name}
                Last Name: {last_name}
                Email: {from_email}
                Message: {message}
             """

             # Your data processing goes here (e.g., print, email)
             print(f"First Name: {first_name}")  # Print data
             try:
                 send_mail(
                     subject,
                     email_body,
                     from_email,
                     ["inhlosoyetfu@gmail.com"],
                 )
                 messages.info(request, "Your email has been sent.")
             except Exception as e:
                 print(f"Error sending email: {e}")  # Print error message for debugging
                 messages.error(request, "Something went wrong. Please try again later.")
             return redirect('contact-us')

         else:
             message.error(request, "Something went wrong.")

    
     return render(request, 'core/contact-us.html', {})