from django import forms
from .models import Driver, DriverProfile
# from .models Passenger, PassengerProfile, DriverReview, PassengerReview, TravelPlan


class NewDriver(forms.ModelForm):
    '''
    Class to create a form for a user to sign up as a driver
    '''
    class Meta:
        model = Driver
        fields = ('first_name', 'last_name', 'phone_number')
