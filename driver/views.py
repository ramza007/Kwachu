from django.shortcuts import render

# Create your views here.
def driverhome(request):
    return render(request, 'driver-home.html')