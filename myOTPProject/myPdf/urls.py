#path setting for generatePdf app
from django.urls import path
from . import views
urlpatterns = [
    path('show/<int:teacher_id>/', views.generate_pdf, name='generate_pdf'),
]