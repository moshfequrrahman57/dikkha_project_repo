


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import os
from django.conf import settings
from myQRCode.utils import generate_qr
from django.shortcuts import render

def generate_pdf(request,teacher_id):
    verification_url = "https://example.com/verify?token=abc123"
    qr_code = generate_qr(verification_url)
    logo_path = os.path.join(settings.STATIC_ROOT, 'myPdf/images/bg3.png')
    print(logo_path)
    context = {
        
        'name': 'মোঃ মুনতাসির আবিদ',
        'course': 'Basic ICT Training For Teachers',
        'date': '2024-06-01',
        'qr_code': qr_code,
        

        }
    
    

    html_string = render_to_string('myPdf/certificate.html', context)
    
   
    html = HTML(string=html_string, base_url=settings.STATIC_ROOT)
    pdf = html.write_pdf(stylesheets=[CSS(os.path.join(settings.STATIC_ROOT, 'myPdf/css/style.css'))])
    
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="generated_report.pdf"'
    
    return response

