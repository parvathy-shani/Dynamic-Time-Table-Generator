from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Department, Timeslots, Rooms, Lecturers, Courses
from .forms import UpdateDepartmentForm, UpdateRoomForm, UpdateLecturerForm, UpdateCourseForm, UpdateTimeslotForm
import json
import logging
import requests
from django.http import HttpResponseNotAllowed

logger = logging.getLogger(__name__)

User = get_user_model()

def home(request):
    return render(request,"authentication/index.html")

def register(request):
    return render(request,"authentication/register.html")

@login_required(login_url='/login/')
def student(request):
    return render(request, "authentication/Dashboard _student.html")

@login_required(login_url='/login/')
def teacher(request):
    return render(request, "authentication/Dashboard_Teacher.html")

@login_required(login_url='/login/')
def institution(request):
    return render(request, "authentication/Dashboard_institution.html")

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        role = request.POST['role']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if role == 'Teacher':
                if User.objects.filter(username=username).values()[0]['is_teacher']:
                    return redirect('teacher')
                else:
                    return(redirect('login'))
            elif role == 'Institution_head':
                if User.objects.filter(username=username).values()[0]['is_inst']:
                    return redirect('institution')
                else:
                    return(redirect('login'))
                
            elif role == 'Student':
                if User.objects.filter(username=username).values()[0]['is_student']:
                    return redirect('student')
                else:
                    return(redirect('login'))
                
        else:
            messages.error(request, "Credentials don't match")
            return redirect('home')
        

    return render(request,"authentication/log_in.html")

def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def register_student(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mailid']
        password = request.POST['pwd']
        conf_password = request.POST['cpwd']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_student = True
        myuser.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    else:
        # Handle GET request (display the registration form)
        return render(request, 'authentication/register_student.html')
    
def register_teacher(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mailid']
        password = request.POST['pwd']
        conf_password = request.POST['cpwd']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_teacher = True

        myuser.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    else:
        # Handle GET request (display the registration form)
        return render(request, 'authentication/register_teacher.html')

def register_institution(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mailid']
        password = request.POST['pwd']
        conf_password = request.POST['cpwd']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_inst = True

        myuser.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    else:
        # Handle GET request (display the registration form)
        return render(request, 'authentication/register_institution.html')
    
def department_data(request, pk):
    department = Department.objects.get(id=pk)
    context = {'department': department}
    return render(request, 'authentication/Department_data.html', context)

@login_required(login_url='/login/')
def create_department(request):
    context = {} 

    if request.method == "POST":
        department_names = request.POST.getlist('Dept_name')
        for name in department_names:
            department = Department(name=name, host=request.user)
            department.save()
        return redirect('workspace_institution')
    
    departments = Department.objects.all()
    context['departments'] = departments
    

    return render(request, "authentication/Create_department.html", context)

@login_required(login_url='/login/')
def create_rooms(request, pk):
    department = Department.objects.get(id=pk)
    
    room_context = {}

    if request.method == 'POST':
        room_names = request.POST.getlist('roomName[]')
        allotted_batches = request.POST.getlist('allotted_batch[]')
        purposes = request.POST.getlist('purpose[]')

        for name, allotted_batch, purpose in zip(room_names, allotted_batches, purposes):
            room = Rooms(department=department, roomName=name, allottedBatch=allotted_batch, purpose=purpose)
            room.save()
        
        return redirect('department_data', pk=pk)

    # Fetch all rooms for display
    rooms = Rooms.objects.all()
    room_context['rooms'] = rooms
     
    return render(request, 'authentication/Create_rooms.html', room_context)

@login_required(login_url='/login/')
def create_lecturers(request,pk):
    department = Department.objects.get(id=pk)

    lecturer_context = {}

    if request.method == 'POST':
        lecturer_names = request.POST.getlist('lecturerName[]')
        lecturer_positions = request.POST.getlist('lecturerPosition[]')
        preferred_timeslots = request.POST.getlist('preferredTimeslot[]')

        for lecturer_name, lecturer_position,  preferred_timeslot in zip(lecturer_names, lecturer_positions, preferred_timeslots):
            lecturer = Lecturers(department = department, lecturerName = lecturer_name, position = lecturer_position, preferredTimeslot = preferred_timeslot)
            lecturer.save()

        return redirect('department_data', pk=pk)

    lecturers = Lecturers.objects.all()
    lecturer_context['lecturers'] = lecturers

    return render(request,'authentication/Create_lecturers.html', lecturer_context)

@login_required(login_url='/login/')
def create_courses(request, pk):
    department = Department.objects.get(id=pk)
    course_context = {}

    if request.method == 'POST':
        course_names = request.POST.getlist('course_name[]')
        course_codes = request.POST.getlist('course_code[]')
        course_types = request.POST.getlist('section[]')
        course_allotted_batches = request.POST.getlist('allotted_batch[]')

        for course_name, course_code,  course_type, course_allotted_batch in zip(course_names, course_codes, course_types, course_allotted_batches):
            course = Courses(department = department, courseName = course_name, courseCode = course_code , type = course_type, allottedBatch = course_allotted_batch)
            course.save()

        return redirect('department_data', pk=pk)
    
    courses = Courses.objects.all()
    course_context['courses'] = courses

    return render(request,'authentication/Create_courses.html', course_context)

@login_required(login_url='/login/')
def create_timeslots(request, pk):
    department = Department.objects.get(id=pk)
    timeslot_context = {}

    if request.method == "POST":
        days = request.POST.getlist('day[]')
        start_times = request.POST.getlist('startHour[]')
        end_times = request.POST.getlist('endHour[]')

        
        for day, start_time,  end_time in zip(days, start_times, end_times):
            timeslot = Timeslots(department=department, day=day, startTime=start_time, endTime=end_time)
            timeslot.save()

        return redirect('department_data', pk=pk)  # Redirect to a success URL after saving
    
    timeslots =Timeslots.objects.all()
    timeslot_context['timeslots'] = timeslots

    return render(request, 'authentication/Create_timeslots.html', timeslot_context)


@login_required(login_url='/login/')
def update_department(request, pk):
    department = Department.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateDepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('workspace_institution')
    else:
        form = UpdateDepartmentForm(instance=department)

    context = {'form': form}
    return render(request, 'authentication/Update_department.html', context)

@login_required(login_url='/login/')
def update_rooms(request, pk):
    room = Rooms.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('create_rooms', pk=pk)
    else:
        form = UpdateRoomForm(instance=room)

    context = {'form': form}
    return render(request, 'authentication/Update_rooms.html', context)

@login_required(login_url='/login/')
def update_lecturers(request, pk):
    lecturer = Lecturers.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateLecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            dept_id =  lecturer.department.id
            return redirect('create_lecturers', pk=dept_id)
    else:
        form = UpdateLecturerForm(instance=lecturer)

    context = {'form': form}

    return render(request, 'authentication/Update_lecturers.html', context)

@login_required(login_url='/login/')
def update_courses(request, pk):
    course = Courses.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            dept_id =  course.department.id
            return redirect('create_courses', pk=dept_id)
    else:
        form = UpdateCourseForm(instance=course)

    context = {'form': form}
    return render(request,'authentication/Update_courses.html', context)

@login_required(login_url='/login/')
def update_timeslots(request, pk):
    timeslot = Timeslots.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateTimeslotForm(request.POST, instance=timeslot)
        if form.is_valid():
            form.save()
            dept_id =  timeslot.department.id
            return redirect('create_timeslots', pk=dept_id)
    else:
        form = UpdateTimeslotForm(instance=timeslot)

    context = {'form': form}
    return render(request,'authentication/Update_timeslots.html', context)

@login_required(login_url='/login/')
def delete_department(request,pk):
    context = {}
    department = Department.objects.get(pk=pk)
    context['departments'] = department
    if request.method == 'POST':
        department.delete()
        return redirect('workspace_institution') 
    return render(request, "authentication/Delete_department.html", {department: department})

@login_required(login_url='/login/')
def delete_rooms(request,pk):
    context = {}
    room = Rooms.objects.get(pk=pk)
    context['rooms'] = room
    if request.method == 'POST':
        room.delete()
        return redirect('create_rooms', pk=pk) 
    return render(request, "authentication/Delete_department.html", {room: room})

@login_required(login_url='/login/')
def delete_lecturers(request, pk):
    context = {}
    lecturer = Lecturers.objects.get(pk=pk)
    context['lecturer'] = lecturer  
    if request.method == 'POST':
        lecturer.delete()
        dept_id =  lecturer.department.id
        return redirect('create_lecturers', pk=dept_id) 
    return render(request, "authentication/Delete_department.html", context)

@login_required(login_url='/login/')
def delete_courses(request, pk):
    context = {}
    course = Courses.objects.get(pk=pk)
    context['course'] = course 
    if request.method == 'POST':
        course.delete()
        dept_id =  course.department.id
        return redirect('create_courses', pk=dept_id) 
    return render(request,'authentication/Delete_courses.html', context)

@login_required(login_url='/login/')
def delete_timeslots(request, pk):
    context = {}
    timeslot = Timeslots.objects.get(pk=pk)
    context['timeslot'] = timeslot
    if request.method == 'POST':
        timeslot.delete()
        dept_id =  timeslot.department.id
        return redirect('create_timeslots', pk=dept_id) 
    return render(request,'authentication/Delete_timeslots.html', context)

@login_required(login_url='/login/')
def workspace_institution(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'authentication/Workspace_institution.html', context)

@login_required(login_url='/login/')
def timetable_institution(request):
    return render(request,'authentication/Timetable_institution.html')

@login_required(login_url='/login/')
def timetable_teacher(request):
    return render(request,'authentication/Timetable_teacher.html')

@login_required(login_url='/login/')
def timetable_student(request):
    return render(request,'authentication/Timetable_student.html')

@login_required(login_url='/login/')
def timetable_data_sample(request):
    # Make a GET request to your API view to fetch the JSON data
    response = requests.get('http://127.0.0.1:8000/api/v1/display_generation/').json()
    print(response)
    return render(request, 'authentication/timetable_data_sample.html', {'responses': response})