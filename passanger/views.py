from django.shortcuts import render

# Create your views here.
def passanger(request):
    return render (request, 'passanger-home.html')