from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'gisystem/about.html', {})


def campus_overview(request):
    return render(request, 'gisystem/map.html', {})


def about(request):
    return render(request, 'gisystem/about.html', {})


def contact(request):
    return render(request, 'gisystem/contact.html', {})


def overview(request):
    return render(request, 'gisystem/overview.html', {})


def hall(request):
    return render(request, 'gisystem/hall.html', {})
