from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('trainees/', views.trainees_list, name='trainees_list'),
    path('add-trainee/', views.add_trainee, name='add_trainee'),
    path('add-authority/', views.add_certificate_authority, name='add_certificate_authority'),
    path('success/', views.success_signature_upload, name='success_signature_upload'),  # সেভ হওয়ার পর যেখানে পাঠাতে চান
]