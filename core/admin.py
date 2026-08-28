from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'major', 'gpa', 'is_active', 'enrollment_date')
    list_filter = ('is_active', 'major')
    search_fields = ('name', 'email')
