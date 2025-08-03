from django.shortcuts import render

def index(request):
    context = {
        'greeting': 'Hello, Birungi!'
    }
    return render(request, 'index.html', context)
