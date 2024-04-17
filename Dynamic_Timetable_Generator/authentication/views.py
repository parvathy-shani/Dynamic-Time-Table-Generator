from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import authentication

def home(request):
    return render(request,"authentication/index.html")

def register(request):
    return render(request,"authentication/register.html")

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        role = request.POST['role']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if role == 'Teacher':
                return render(request, "authentication/Dashboard_Teacher.html")
            elif role == 'Institution_head':
                return render(request, "authentication/Dashboard_institution.html")
            elif role == 'Student':
                return render(request, 'authentication/Dashboard_Student.html')
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

        myuser.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    else:
        # Handle GET request (display the registration form)
        return render(request, 'authentication/register_institution.html')