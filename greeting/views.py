from django.shortcuts import render

# Django view function to render the homepage
def index(request):
    context = {
        'greeting': 'Hello, Birungi!'  # You can personalize this further
    }
    return render(request, 'index.html', context)
