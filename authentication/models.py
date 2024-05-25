from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_inst = models.BooleanField(default=False)

class Department(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ['-updated', '-created']  

    def __str__(self):
        return self.name
    

class Rooms(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    roomName = models.CharField(max_length=50)
    allottedBatch = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.roomName} - {self.allottedBatch}-{self.purpose}"
    
class Lecturers(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lecturerName = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    preferredTimeslot = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.lecturerName}-{self.position}-{self.preferredTimeslot}"
    
class Courses(models.Model):  
    department = models.ForeignKey(Department, on_delete=models.CASCADE) 
    courseName = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    allottedBatch = models.CharField(max_length=50)
    courseCode = models.CharField(max_length=50, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.courseName}-{self.courseCode}-{self.type}-{self.allottedBatch}"

    
class Timeslots(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    day = models.CharField(max_length=50)
    startTime = models.CharField(max_length=50)
    endTime =  models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['created']  

    def __str__(self):
        return self.day