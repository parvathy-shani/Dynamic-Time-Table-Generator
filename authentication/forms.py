# In forms.py
from django import forms
from .models import Department, Rooms, Lecturers, Courses, Timeslots

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']  # Include other fields as needed for update

class UpdateRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['roomName', 'allottedBatch', 'purpose']

class UpdateLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturers
        fields = ['lecturerName', 'position', 'preferredTimeslot']

class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['courseName', 'type', 'allottedBatch', 'courseCode']

class UpdateTimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslots
        fields = ['day', 'startTime', 'endTime']