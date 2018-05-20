from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Create your models here.


class Driver(models.Model):
    '''
    Class that defines a Driver in the application
    '''
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def get_drivers(cls):
        '''
        Function that gets all the drivers in the database
        '''
        drivers = Driver.objects.all()

        return drivers


class DriverProfile(models.Model):
    '''
    Class that defines a profile for a Driver
    '''
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        blank=True, upload_to="driver/profile-pic")
        # , default=DEFAULTDRIVERPROFILEPIC)
    car_image = models.ImageField(
        blank=True, upload_to="car-image/")
        # , default=DEFAULTCAR)
    car_capacity = models.PositiveIntegerField(default=0, blank=True)
    car_number_plate = models.CharField(blank=True, max_length=255)
    car_color = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.driver.first_name + ' ' + self.driver.last_name

    @classmethod
    def get_driver_profiles(cls):
        '''
        Function that gets all the driver profiles in the database
        '''
        driver_profiles = DriverProfile.objects.all()

        return driver_profiles

# Create Driver Profile when creating a Driver


# @receiver(post_save, sender=Driver)
def create_driverprofile(sender, instance, created, **kwargs):
    if created:
        DriverProfile.objects.create(driver=instance)

# Save Driver Profile when saving a Driver


# @receiver(post_save, sender=Driver)
def save_driverprofile(sender, instance, **kwargs):
    instance.driverprofile.save()
