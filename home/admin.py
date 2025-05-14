from django.contrib import admin
from .models import Student

class adminStudent(admin.ModelAdmin):
    list_display = ('regNo', 'name', 'feeBal')

# Register your models here.
admin.site.register(Student, adminStudent)
