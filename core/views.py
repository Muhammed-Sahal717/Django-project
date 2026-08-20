from django.shortcuts import render


def home_view(request):
    context = {
        'app_name': 'My Awesome Django App',
        'subtitle': 'A minimal, lightning-fast foundation for building modern web applications.',
        'features': ['Fast', 'Secure', 'Scalable', 'Modern'],
    }
    return render(request, 'home.html', context)

def about_view(request):
    context = {
        'cards': [
            {
                'title': 'Our Mission',
                'description': 'To simplify the development process and provide robust architectural patterns out of the box.'
            },
            {
                'title': 'Our Stack',
                'description': 'Django, Python, and modern CSS methodologies to keep things lightweight.'
            },
            {
                'title': 'Community',
                'description': 'Open source at heart, we value contributions and collaborative learning.'
            }
        ]
    }
    return render(request, 'about.html', context)