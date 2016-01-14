from django.contrib import admin
from .models import Student, Group
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']

admin.site.register(Student)
admin.site.register(Group, GroupAdmin)
