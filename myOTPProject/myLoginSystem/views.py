from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OtpserviceTrainees



# Create your views here.
def login_view(request):
    return HttpResponse("This is the login page.")

def logout_view(request):
    return HttpResponse("This is the logout page.")

def register_view(request):
    return HttpResponse("This is the registration page.")

#view for displaying all trainees
def trainees_list(request):
    trainees = OtpserviceTrainees.objects.all()
    return render(request, 'myLoginSystem/trainees_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        roll_number = request.POST.get('roll_number')
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')

        trainee = OtpserviceTrainees(
            year=year,
            course=course,
            batch=batch,
            roll_number=roll_number,
            name=name,
            mobile_number=mobile_number
        )
        trainee.save()
        return redirect('trainees_list')
    return render(request, 'myLoginSystem/add_trainee.html')
    
