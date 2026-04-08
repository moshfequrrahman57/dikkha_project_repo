from django.shortcuts import render
from django.http import HttpResponse
import secrets
import string, json
import requests

# Create your views here.
#view for otp generate form

def otp_generate_form(request):
    otp_str = ''.join(secrets.choice(string.digits) for _ in range(6))
    request.session['generated_otp'] = otp_str
    return render(request, 'otpApp/otp_generate_form.html')

def otp_send(request):
    otp= request.session.get('generated_otp')
    phone_number = request.POST.get('phone_number')
    print(f"Generated Nom OTP: {otp}, Phone Number: {phone_number}")
    url = "https://api.mimsms.com/api/SmsSending/SMS"
    api_key = "6RHBKFUG3CX9RRH"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
        
    }
    payload = {
                "UserName": "moshfequrrahman57@gmail.com",
                "Apikey": "6RHBKFUG3CX9RRH",
                "MobileNumber": f"{phone_number}",
                "CampaignId": "null",
                "SenderName": "Bismillah",
                "TransactionType": "T",
                "Message": f" Assalamualikum from Noman. Your OTP is {otp}"
                }
    try:
        response =requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return HttpResponse(f"OTP {otp} sent to {phone_number} successfully!")
        else:
            return HttpResponse(f"Failed to send OTP. Status code: {response.status_code}, Response: {response.text}")
            
    except Exception as e:
        return HttpResponse(f"An exception error occurred: {str(e)}")


    # return HttpResponse(f"OTP {otp} sent to {phone_number} successfully!")



def otp_verify_form(request):
    return render(request, 'otpApp/otp_verify_form.html')

def otp_verify(request):
    return HttpResponse("OTP verified successfully!")
    