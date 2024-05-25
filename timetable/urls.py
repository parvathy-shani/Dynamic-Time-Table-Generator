from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, LecturerViewSet, CoursesViewSet, TimeslotsViewSet

# Create a router and register the RoomViewSet with it
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'timeslots', TimeslotsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('generator/',views.generator, name="generator"),
    path('timeslots_details/', views.timeslots_details, name='timeslots_details'),
    path('rooms_details/', views.rooms_details, name='rooms_details'), 
    path('lecturers_details/', views.lecturers_details, name='lecturers_details'),
    path('courses_details/', views.courses_details, name='courses_details'),
    path('display_generation/', views.display_generation, name='display_generation'),
]