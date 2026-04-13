
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import CSS, HTML

from myOTPProject import settings
import os

def generate_pdf(request, teacher_id):
    # ডাটাবেস থেকে শিক্ষকের তথ্য আনা
    teacher_data = {'name': 'মোঃ মুনতাসির আবিদ', 'course': 'ICT Training'}
    
    # HTML টেম্পলেটকে স্ট্রিং এ রূপান্তর
   
    css_path = os.path.join(settings.BASE_DIR, 'myPdf', 'static', 'myPdf', 'css', 'style.css')
    html_string = render_to_string('myPdf/certificate.html', {'font_path': css_path, 'teacher_data': teacher_data})
    html = HTML(string=html_string, base_url=str(settings.BASE_DIR))
    # পিডিএফ তৈরি
    pdf = html.write_pdf()
    
    # ব্রাউজারে পিডিএফ রেসপন্স পাঠানো
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="certificate.pdf"'
    return response
