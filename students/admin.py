from django.contrib import admin
from .models import Student, Group
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'student_group']

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
