from rest_framework import serializers
from authentication.models import Rooms, Lecturers, Courses, Timeslots

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['roomName', 'allottedBatch', 'purpose']

class LecturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturers
        fields = ['lecturerName', 'position', 'preferredTimeslot']

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['courseName', 'type', 'allottedBatch', 'courseCode']

class TimeslotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslots
        fields = ['day', 'startTime', 'endTime']