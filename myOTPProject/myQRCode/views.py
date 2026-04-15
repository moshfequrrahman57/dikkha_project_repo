from django.shortcuts import render
from django.http import HttpResponse

import qrcode
from io import BytesIO
import base64

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the QR Code Generator!")


