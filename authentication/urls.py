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

    path('authentication/Dashboard_student/',views.student, name='student'),
    path('authentication/register_student/', views.register_student, name='register_student'),
    path('authentication/register_teacher/', views.register_teacher, name='register_teacher'),
    path('authentication/register_institution/', views.register_institution, name='register_institution'),

    path('authentication/timetable_institution/', views.timetable_institution, name="timetable_institution"),
    path('authentication/timetable_teacher/', views.timetable_teacher, name="timetable_teacher"),
    path('authentication/timetable_student/', views.timetable_student, name="timetable_student"),

    path('authentication/workspace_institution/', views.workspace_institution, name='workspace_institution'),
    path('authentication/create_department', views.create_department, name='create_department'),
    path('authentication/update_department/<str:pk>/', views.update_department, name='update_department'),
    path('authentication/delete_department/<str:pk>/', views.delete_department, name='delete_department'),

    path('authentication/Department_data/<str:pk>/', views.department_data, name='department_data'),
    path('authentication/create_rooms/<str:pk>/', views.create_rooms, name="create_rooms"),
    path('authentication/update_rooms/<str:pk>/', views.update_rooms, name='update_rooms'),
    path('authentication/delete_rooms/<str:pk>/', views.delete_rooms, name='delete_rooms'),
    path('authentication/create_lecturers/<str:pk>/', views.create_lecturers, name="create_lecturers"),
    path('authentication/update_lecturers/<str:pk>/', views.update_lecturers, name="update_lecturers"),
    path('authentication/delete_lecturers/<str:pk>/', views.delete_lecturers, name="delete_lecturers"),
    path('authentication/create_courses/<str:pk>/', views.create_courses, name="create_courses"),
    path('authentication/update_courses/<str:pk>/', views.update_courses, name="update_courses"),
    path('authentication/delete_courses/<str:pk>/', views.delete_courses, name="delete_courses"),
    path('authentication/create_timeslots/<str:pk>/', views.create_timeslots, name="create_timeslots"),
    path('authentication/update_timeslots/<str:pk>/', views.update_timeslots, name="update_timeslots"),
    path('authentication/delete_timeslots/<str:pk>/', views.delete_timeslots, name="delete_timeslots"),

    path('authentication/timetable_data_sample/', views.timetable_data_sample, name="timetable_data_sample"),

]