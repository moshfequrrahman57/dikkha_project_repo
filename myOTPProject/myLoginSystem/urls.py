from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('trainees/', views.trainees_list, name='trainees_list'),
    path('add-trainee/', views.add_trainee, name='add_trainee'),
]