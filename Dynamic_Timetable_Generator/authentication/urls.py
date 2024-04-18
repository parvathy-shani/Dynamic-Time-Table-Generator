from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('teacher/',views.teacher, name='teacher'),
    path('institution/',views.institution, name='institution'),
    path('student/',views.student, name='student'),
    path('authentication/register_student/', views.register_student, name='register_student'),
    path('authentication/register_teacher/', views.register_teacher, name='register_teacher'),
    path('authentication/register_institution/', views.register_institution, name='register_institution'),
]