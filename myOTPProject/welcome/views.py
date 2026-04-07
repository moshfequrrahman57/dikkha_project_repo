from django.shortcuts import render

# Create your views here.
#wecome message to the user 
def welcome(request):
    return render(request, 'welcome/welcome.html')