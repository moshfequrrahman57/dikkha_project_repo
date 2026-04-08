from django.urls import path
from . import views

urlpatterns = [ 
    path ('generate/', views.otp_generate_form, name='otp_generate_form'),
    path ('verify/', views.otp_verify_form, name='otp_verify_form'),
    path ('generate/send/', views.otp_send, name='otp_send'),
    path ('verify/submit/', views.otp_verify, name='otp_verify'),

]
