


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

def generate_pdf(request,teacher_id):
    print(f"Request scheme: {request.scheme}, Host: {request.get_host()}, Path: {request.path}")
    # 1. Prepare data for the template
    context = {'some_variable': 'মোঃ মোশফেকুর রহমান '}
    
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

