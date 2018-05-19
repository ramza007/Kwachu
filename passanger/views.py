from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Passenger, PassengerProfile
from .forms import NewPassenger, PassengerLogin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

# Create your views here.
def passanger(request):
    return render (request, 'passanger-home.html')


def new_passenger(request):
    '''
    View function to display a registration form when the user selects the passenger option
    '''
    title = 'Sign Up Passenger'

    if request.method == 'POST':

        form = NewPassenger(request.POST)

        if form.is_valid:

            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            phone_number = request.POST.get('phone_number')

            new_passenger = Passenger(
                first_name=first_name, last_name=last_name, phone_number=phone_number)

            passengers = Passenger.objects.all()

            for existing_passenger in passengers:

                if int(new_passenger.phone_number) != int(existing_passenger.phone_number):
                    continue

                elif int(new_passenger.phone_number) == int(existing_passenger.phone_number):
                    message = 'The number is already registered'

                    messages.error(
                        request, ('This number is already registered'))

                    return render(request, 'registration/registration_form-passanger.html', {"title": title, "form": form, "message": message})

                    break

            new_passenger.save()

            return redirect(passenger, new_passenger.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        form = NewPassenger()

        return render(request, 'registration/registration_form-passanger.html', {"title": title, "form": form})


def passenger_login(request):
    '''
    View function to display login form for a passenger
    '''
    title = "Sign In Passenger"

    if request.method == 'POST':

        form = PassengerLogin(request.POST)

        if form.is_valid:

            phone_number = request.POST.get('phone_number')

            try:
                found_passenger = Passenger.objects.get(
                    phone_number=phone_number)

                return redirect(passenger, found_passenger.id)

            except ObjectDoesNotExist:
                raise Http404()

        else:

            messages.error(request, ('Please correct the error below.'))

    else:
        form = PassengerLogin()

        return render(request, 'registration/login-passanger.html', {"title": title, "form": form})

# Passenger homepage is Profile page


# def passenger(request, id):
#     '''
#     View function to display an authenticated logged in passenger's profile
#     '''
#     passengers = Passenger.objects.all()

#     try:

#         passenger = Passenger.objects.get(id=id)

#         if passenger in passengers:

#             title = f'{passenger.first_name} {passenger.last_name}'

#             passenger_profile = PassengerProfile.objects.get(
#                 passenger=passenger)

#             return render(request, 'all-passengers/profile.html', {"title": title, "passenger": passenger, "passenger_profile": passenger_profile})

#         else:
#             return redirect(passenger_login)

#     except ObjectDoesNotExist:
#         return redirect(new_passenger)

#         # raise Http404()
