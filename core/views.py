from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


def dashboard_view(request):
    students = Student.objects.all().order_by('-gpa')
    context = {
        'students': students,
        'total_students': students.count(),
        'active_students': students.filter(is_active=True).count(),
    }
    return render(request, 'dashboard.html', context)

def platform_info_view(request):
    return render(request, 'platform_info.html')

def add_student_view(request):
    # 1. If this is a POST request, the user submitted the form
    if request.method == 'POST':
        form = StudentForm(request.POST) # Bind the form with submitted data
        if form.is_valid(): # Django automatically validates the data
            form.save()     # Saves the new student to the database
            return redirect('dashboard') # Send them back to the dashboard
    else:
        # 2. If it's a GET request, just show an empty form
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})
