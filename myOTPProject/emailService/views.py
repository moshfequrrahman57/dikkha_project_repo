from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def email_input_form(request):
    return render(request, 'emailService/email_input_form.html')

def email_send(request):
    email = request.POST.get('email')
    print(f"Email entered: {email}")
    subject = "Test Email from Noman dikkha"
    message = "This is a test email sent from the banbeis dikkha  Email  application. Here used " \
    "gmail smtp server"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    # Here you would typically add logic to send an email using a service like SMTP or an API
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse(f"Email sent to {email} successfully!")