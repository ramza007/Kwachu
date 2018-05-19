from django import forms
from .models import Passenger, PassengerProfile
# from .models import PassengerReview, TravelPlan


class NewPassenger(forms.ModelForm):
    '''
    Class to create a form for a user to sign up as a driver
    '''
    class Meta:
        model = Passenger
        fields = ('first_name', 'last_name', 'phone_number')


class PassengerLogin(forms.ModelForm):
    '''
    Class to create a form for a user to sign in as a passenger
    '''
    class Meta:
        model = Passenger
        fields = ('phone_number',)


# class UpdatePassengerProfile(forms.ModelForm):
#     '''
#     Class to create a form for a passenger to change their profile
#     '''
#     class Meta:
#         model = PassengerProfile
#         fields = ('gender', 'profile_pic', 'general_location')



# class ReviewPassengerForm(forms.ModelForm):
#     '''
#     Class to create a form for reviewing a passenger
#     '''
#     class Meta:
#         model = PassengerReview
#         fields = ('review_content',)


# class NewTravelPlan(forms.ModelForm):
#     '''
#     Class to create a form for creating a new travel plan
#     '''
#     class Meta:
#         model = TravelPlan
#         exclude = ['driver_profile', 'travel_date']
#         fields = ('current_location', 'destination')
