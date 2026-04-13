from django.urls import path
from . import views

urlpatterns = [
    path('email-input/', views.email_input_form, name='email_input_form'),
    path('email-send/', views.email_send, name='email_send'),
]