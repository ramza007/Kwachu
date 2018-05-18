from django.contrib import admin
from .models import Passenger, PassengerProfile

# Register your models here.

admin.site.register(Passenger)
admin.site.register(PassengerProfile)
