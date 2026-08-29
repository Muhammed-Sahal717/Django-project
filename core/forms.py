from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'major', 'gpa', 'is_active')
        # We can add CSS classes to our form inputs directly here!
        widgets = {  # noqa: RUF012
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Jane Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'jane@example.com'}),
            'major': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Computer Science'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'placeholder': '4.00'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
