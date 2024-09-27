from django.shortcuts import render


def portfolio_view(request):
    # Example data: list of dictionaries representing each project
    projects = [
        {
            'name': 'Weather API',
            'skills': 'Python, Django, API',
            'github_url': 'https://github.com/your_github/weather-api',
            'live_url': 'http://yourliveapp.com/weather-api'
        },
        {
            'name': 'To-Do App',
            'skills': 'Python, Django, JavaScript',
            'github_url': 'https://github.com/your_github/todo-app',
            'live_url': 'http://yourliveapp.com/todo-app'
        },
        # Add more projects as needed
    ]

    # Pass the projects list to the template
    return render(request, 'portfolio/index.html', {'projects': projects})
