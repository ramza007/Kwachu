from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Create your models here.


class Passenger(models.Model):
    '''
    Class that defines a Passenger in the application
    '''
    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def get_passengers(cls):
        '''
        Function that gets all the passengers in the database
        '''
        passengers = Passenger.objects.all()

        return passengers


class PassengerProfile(models.Model):
    '''
    Class that defines a profile for a Passenger
    '''
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    # profile_pic = models.ImageField(
    #     blank=True, upload_to="passenger/profile-pic", default=DEFAULTPASSANGERPROFILEPIC)


    general_location = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.passenger.first_name + ' ' + self.passenger.last_name

    @classmethod
    def get_passenger_profiles(cls):
        '''
        Function that gets all the passenger profiles in the database
        '''
        passenger_profiles = PassengerProfile.objects.all()

        return passenger_profiles

# Create Passenger Profile when creating a Passenger


# @receiver(post_save, sender=Passenger)
def create_passengerprofile(sender, instance, created, **kwargs):
    if created:
        PassengerProfile.objects.create(passenger=instance)

# Save Passenger Profile when saving a Passenger


# @receiver(post_save, sender=Passenger)
def save_passengerprofile(sender, instance, **kwargs):
    instance.passengerprofile.save()

#--------------------------------------------#
class state(models.Model):
    name = models.CharField(max_length =50,)
    state_abbr = models.CharField(max_length=3,
        blank = True)


    def username(self):
        return self.state_abbr

class county(models.Model):
    name = models.CharField(max_length=50, blank=True)

