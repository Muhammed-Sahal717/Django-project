from django.shortcuts import render

from .models import Student


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
