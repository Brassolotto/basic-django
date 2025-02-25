from django.shortcuts import render

def index(request):
    """Página principal de Basic Django."""
    return render(request, 'basic_djangos/index.html')
