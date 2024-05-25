from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .encode import encode_timeslots,encode_room,encode_lectures,encode_courses, format_events, format_pairs, chromosome_generation, elitism, selection, crossover, hard_constraints
import itertools
from rest_framework import viewsets
from authentication.models import Rooms, Lecturers, Courses, Timeslots
from .serializers import RoomsSerializer, LecturersSerializer, CoursesSerializer, TimeslotsSerializer

generation = {}

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturers.objects.all()
    serializer_class = LecturersSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class TimeslotsViewSet(viewsets.ModelViewSet):
    queryset = Timeslots.objects.all()
    serializer_class = TimeslotsSerializer

@api_view(['GET'])
def timeslots_details(request):
    timeslots = Timeslots.objects.all()
    serializer = TimeslotsSerializer(timeslots, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)

@api_view(['GET'])
def rooms_details(request):
    rooms = Rooms.objects.all()
    serializer = RoomsSerializer(rooms, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)

@api_view(['GET'])
def lecturers_details(request):
    lecturers = Lecturers.objects.all()
    serializer = LecturersSerializer(lecturers, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)

@api_view(['GET'])
def courses_details(request):
    courses = Courses.objects.all()
    serializer = CoursesSerializer(courses, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)

@api_view(['POST'])
def generator(request):
    if request.method == 'POST':

        #timeslots_data_processing
        timeslots = Timeslots.objects.all()
        serializer_timeslots = TimeslotsSerializer(timeslots, many=True)
        serialized_data_timeslots = serializer_timeslots.data

        input_timeslot = serialized_data_timeslots
        output_timeslot = encode_timeslots(input_timeslot)
        output_timeslot_keys = output_timeslot.keys()

        #rooms_data_processing
        rooms = Rooms.objects.all()
        serializer_rooms = RoomsSerializer(rooms, many=True)
        serialized_data_rooms = serializer_rooms.data

        input_room = serialized_data_rooms
        output_room = encode_room(input_room)
        output_room_keys = output_room.keys()

        #packet formation
        packets = list(itertools.product(output_timeslot_keys, output_room_keys))

        #lecturers_data_processing
        lecturers = Lecturers.objects.all()
        serializer_lecturers = LecturersSerializer(lecturers, many=True)
        serialized_data_lecturers = serializer_lecturers.data

        input_lecturers =serialized_data_lecturers
        output_lectures = encode_lectures(input_lecturers)
        output_lectures_keys = output_lectures.keys()

        #course_data_processong
        courses = Courses.objects.all()
        serializer_courses = CoursesSerializer(courses, many=True)
        serialized_data_courses = serializer_courses.data

        input_courses = serialized_data_courses
        output_courses = encode_courses(input_courses)
        output_courses_keys = output_courses.keys()

        #event formation
        events = list(itertools.product(output_lectures_keys, output_courses_keys))
        formatted_events = format_events(events)

        #packet formation
        pairs = list(itertools.product(packets, formatted_events))
        formatted_pairs = format_pairs(pairs)

        #initial population
        initial_population = chromosome_generation(formatted_pairs)

        #elite population
        elite_population = elitism(initial_population)

        #selection
        selection_population = selection(elite_population)

        #crossover
        crossover_population = crossover(selection_population)

        #Hard constraints
        fitness_score = hard_constraints(crossover_population)

        sum = 0
        for item in fitness_score:
            sum = sum + item # type: ignore
        if sum == 8:
            output_timetable = crossover_population

        timetable_batch = 0
        
        for timetables in output_timetable.values():
            for timetable in timetables:
                TimeTable = []
                for gene in timetable:
                    if gene[0][0] in output_timeslot.keys():
                        timeslot = output_timeslot[gene[0][0]]
                    if gene[0][1] in output_room.keys():
                        room = output_room[gene[0][1]][0]
                        batch = output_room[gene[0][1]][1]
                    if gene[1][0] in output_lectures.keys():
                        lecturer = output_lectures[gene[1][0]][0][0]
                    if gene[1][1] in output_courses.keys():
                        course = output_courses[gene[1][1]][0]
                    slot = f"{timeslot}-{batch}-{room}-{lecturer}-{course}"
                    TimeTable.append(slot)
                generation[timetable_batch] = TimeTable
                timetable_batch = timetable_batch + 1
        


    return Response(generation,status=status.HTTP_200_OK)  # Return the input_timeslot as a response
    
@api_view(['GET'])
def display_generation(request):
    return Response(generation, status=status.HTTP_200_OK)
        