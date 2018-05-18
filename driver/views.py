from django.shortcuts import render
from .forms import NewDriver

# Create your views here.
def driverhome(request):
    return render(request, 'driver-home.html')


def new_driver(request):
    return render(request, 'registration/registration_form.html')
