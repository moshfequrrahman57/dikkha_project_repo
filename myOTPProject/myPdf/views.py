


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import os
from django.conf import settings
from myQRCode.utils import generate_qr

def generate_pdf(request,teacher_id):
    verification_url = "https://example.com/verify?token=abc123"
    qr_base64 = generate_qr(verification_url)
    font_path = os.path.join(settings.BASE_DIR, 'static/myPdf/fonts/kalpurush.ttf')
    print(f"Font path: {font_path}", flush=True)  # Debug: Check if the font path is correct
    # 1. Prepare data for the template
    context = {
        'font_path': font_path,  # Pass the font path to the template
        'name': 'মোছা ইসমত আরা মৌসুমি',
        'qr_base64': qr_base64
        }
    
    
    # 2. Render HTML template to a string
    html_string = render_to_string('myPdf/certificate.html', context)
    
    # 3. Handle Fonts
    # FontConfiguration is required for @font-face or remote Google Fonts to work
    font_config = FontConfiguration()
    
    # 4. Generate PDF
    # base_url ensures relative paths for images/CSS work correctly
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf(font_config=font_config)
    
    # 5. Return PDF as an HTTP Response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="generated_report.pdf"'
    
    return response

