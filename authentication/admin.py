from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, Timeslots, Rooms, Lecturers, Courses

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_teacher', 'is_student', 'is_inst'
        )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Department)
admin.site.register(Timeslots)
admin.site.register(Rooms)
admin.site.register(Lecturers)
admin.site.register(Courses)
