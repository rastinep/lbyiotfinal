from django.shortcuts import render
import serial
import time
from django.http import JsonResponse


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
    serport = serial.Serial('/dev/cu.usbserial', '9600')
    time.sleep(1)
    serport.setDTR(False)
    capacity = serport.readline()
    capacity = capacity.decode('utf-8').rstrip()
    return render(request, 'gisystem/hall.html', {'capacity': capacity})


def ajax_data(request):
    #values = MyNoiseLevelModel.objects.all().values('value')
    json_data = json.dumps(data)
    return Response(json_data, mimetypes='application/json')
