
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_pdf(request, teacher_id):
    # ডাটাবেস থেকে শিক্ষকের তথ্য আনা
    teacher_data = {'name': 'মোঃ মুনতাসির আবিদ', 'course': 'ICT Training'}
    
    # HTML টেম্পলেটকে স্ট্রিং এ রূপান্তর
    html_string = render_to_string('myPdf/certificate.html', teacher_data)
    
    # পিডিএফ তৈরি
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    
    # ব্রাউজারে পিডিএফ রেসপন্স পাঠানো
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="certificate.pdf"'
    return response
