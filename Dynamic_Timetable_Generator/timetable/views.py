from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .encode import encode_timeslots,room,lectures,courses, formatted_pairs, chromosome_generation
import itertools
# Create your views here.

@api_view(['POST'])
def generator(request):
    data = request.data
    if data == {}:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    input_timeslot = data['timeslot']
    input_room = data['classrooms_data']
    output_timeslot = encode_timeslots(input_timeslot)
    output_timeslot_keys = output_timeslot.keys()
    output_room = room(input_room)
    all_combinations = list(itertools.product(output_timeslot_keys, output_room))

    input_lecturers = data['lecturers']
    input_courses = data['courses']

    output_lectures = lectures(input_lecturers)
    output_courses = courses(input_courses)
    all_combinationsz = list(itertools.product(output_lectures.split('\n'), output_courses))
   
    pairs = list(itertools.product(all_combinations,all_combinationsz))

    

    return Response(output_formatted_pairs,status=status.HTTP_200_OK)

