


# def generate_pdf(request, teacher_id):

import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from playwright.async_api import async_playwright
from django.conf import settings

async def generate_pdf(request,teacher_id):
    # 1. Render template to HTML
    context = {'data': 'Your dynamic content here'}
    html_content = render_to_string('myPdf/certificate.html', context)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Create a browser context for isolation
        context = await browser.new_context()
        page = await context.new_page()

        # 2. Load the HTML content
        # 'networkidle' ensures fonts from your static folder are fully loaded
        await page.set_content(html_content, wait_until="networkidle")

        # 3. Generate PDF 
        # print_background=True ensures your CSS colors and fonts appear
        pdf_bytes = await page.pdf(format="A4", print_background=True)
        await browser.close()

    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    return response

    
