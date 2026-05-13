from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    # url = "https://api.mimsms.com/api/SmsSending/SMS"
    api_url = "https://api.sms.net.bd/sendsms"

    # api_key = "6RHBKFUG3CX9RRH"
    api_key = "c9AJ2pyCM0HcEtJkj4sMMHELH7uHn8oVRAzqhaqs"

    headers = {
        "Authorization": f"bearer {api_key}",
        "Content-Type": "application/json"
        
    }
    # payload = {
    #             "UserName": "moshfequrrahman57@gmail.com",
    #             "Apikey": "6RHBKFUG3CX9RRH",
    #             "MobileNumber": f"{phone_number}",
    #             "CampaignId": "null",
    #             "SenderName": "8809617632661",
    #             "TransactionType": "T",
    #             "Message": f"Assalamualikum from Noman. Your OTP is {otp}"
    #             }
    payload = {'api_key': api_key,
    'msg': f'Your smsbd nom OTP is {otp}',
    'to': f'{phone_number}'
    }



    try:
        # response =requests.post(url, data=json.dumps(payload), headers=headers)


        # if response.status_code == 200:
        #     return HttpResponse(f"{response.json()}")
        # else:
        #     return HttpResponse(f"{response.text}")
        response = requests.post(api_url, data=payload, timeout=10)
        response_data = response.json()  # Read JSON data from sms.bd response
            
            # Read specific keys from the JSON structure
        error_code = response_data.get('error')
        msg_text = response_data.get('msg')
            
            # Condition check on the parsed error integer
        if error_code == 0:
                data_payload = response_data.get('data', {})
                request_id = data_payload.get('request_id')
                
                return JsonResponse({
                    "status": "success",
                    "sms_bd_msg": msg_text,
                    "tracking_id": request_id
                })
        else:
            return JsonResponse({
                    "status": "gateway_error",
                    "error_code": error_code,
                    "reason": msg_text
                }, status=400)
                
            
    except Exception as e:
        return HttpResponse(f"An exception error occurred: {str(e)}")


    # return HttpResponse(f"OTP {otp} sent to {phone_number} successfully!")



def otp_verify_form(request):
    return render(request, 'otpApp/otp_verify_form.html')

def otp_verify(request):
    return HttpResponse("OTP verified successfully!")
    