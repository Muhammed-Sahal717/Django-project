import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from core.models import Student


def populate():
    Student.objects.all().delete()
    students_data = [
        ("Alice Johnson", "alice@example.com", "Computer Science", 3.8),
        ("Bob Smith", "bob@example.com", "Mathematics", 3.2),
        ("Charlie Brown", "charlie@example.com", "Physics", 3.9),
        ("Diana Prince", "diana@example.com", "History", 3.5),
        ("Evan Wright", "evan@example.com", "Biology", 2.9),
    ]
    for name, email, major, gpa in students_data:
        Student.objects.create(name=name, email=email, major=major, gpa=gpa, is_active=random.choice([True, True, False]))

if __name__ == '__main__':
    populate()
    print("Database populated successfully.")
