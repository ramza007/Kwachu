from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    html = f'''
        <html>
        <head>
        <title>Kwachu App</title>
        </head>
            <body>
                <h1>Hello Welcome To Kwachu</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
