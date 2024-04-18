from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request,"authentication/index.html")

def register(request):
    return render(request,"authentication/register.html")

@login_required(login_url='/login/')
def student(request):
    return render(request, 'authentication/Dashboard_Student.html')

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