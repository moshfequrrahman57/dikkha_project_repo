
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import CSS, HTML

from myOTPProject import settings
import os

def generate_pdf(request, teacher_id):
    # ডাটাবেস থেকে শিক্ষকের তথ্য আনা
    teacher_data = {'name': 'মোঃ মুনতাসির আবিদ', 'course': 'ICT Training'}
    
    # HTML টেম্পলেটকে স্ট্রিং এ রূপান্তর
    html_string = render_to_string('myPdf/certificate.html', teacher_data)
    css_path = os.path.join(settings.BASE_DIR, 'myPdf', 'static', 'myPdf', 'css', 'style.css')
    
    
    # পিডিএফ তৈরি
    html = HTML(string=html_string,base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf(stylesheets=[CSS(filename=css_path)])
    
    # ব্রাউজারে পিডিএফ রেসপন্স পাঠানো
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="certificate.pdf"'
    return response
