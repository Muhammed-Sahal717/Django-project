from django.shortcuts import render


def home_view(request):
    context = {
        'app_name': 'My Awesome Django App',
        'subtitle': 'A minimal, lightning-fast foundation for building modern web applications.',
        'features': ['Fast', 'Secure', 'Scalable', 'Modern'],
    }
    return render(request, 'home.html', context)