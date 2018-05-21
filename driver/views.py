from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
# from django.contrib.auth.decorators import login_required
from .forms import Driver, NewDriver, DriverLogin
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib import messages

# Create your views here.
def driverhome(request):
    return render(request, 'driver-home.html')


def new_driver(request):
    '''
    View function to display a registration form when the user selects the driver option
    '''
    title = 'Sign Up Driver'

    if request.method == 'POST':

        form = NewDriver(request.POST)

        if form.is_valid:

            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            phone_number = request.POST.get('phone_number')

            new_driver = Driver(first_name=first_name,
                                last_name=last_name, phone_number=phone_number)

            drivers = Driver.objects.all()

            for existing_driver in drivers:

                if int(new_driver.phone_number) != int(existing_driver.phone_number):
                    continue

                elif int(new_driver.phone_number) == int(existing_driver.phone_number):

                    message = 'The number is already registered'

                    messages.error(
                        request, ('This number is already registered'))

                    return render(request, 'registration/registration_form.html', {"title": title, "form": form, "message": message})

                    break

            new_driver.save()

            return redirect(driver, new_driver.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        form = NewDriver()

        return render(request, 'registration/registration_form.html', {"title": title, "form": form})


def driver_login(request):
    '''
    View function to display login form for a driver
    '''
    title = "Sign In Driver"

    try:

        if request.method == 'POST':

            form = DriverLogin(request.POST)

            if form.is_valid:

                phone_number = request.POST.get('phone_number')

                try:
                    found_driver = Driver.objects.get(
                        phone_number=phone_number)

                    return redirect(driver, found_driver.id)

                except ObjectDoesNotExist:
                    raise Http404()

            else:

                messages.error(request, ('Please correct the error below.'))

        else:
            form = DriverLogin()

            return render(request, 'registration/login.html', {"title": title, "form": form})

    except ObjectDoesNotExist:
        return redirect(new_driver)
        # raise Http404()


def driver(request, id):
    '''
    View function to display an authenticated logged in driver's profile
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=id)

        if driver in drivers:

            title = f'{driver.first_name} {driver.last_name}'

            driver_profile = DriverProfile.objects.get(driver=driver)

            return render(request, 'profile.html', {"title": title, "driver": driver, "driver_profile": driver_profile})

        else:
            return redirect(driver_login)

    except ObjectDoesNotExist:
        return redirect(new_driver)
        # raise Http404()


@transaction.atomic
def update_driver_profile(request, id):
    '''
    View function to display an update driver profile form for an authenticated driver
    '''
    drivers = Driver.objects.all()

    try:

        found_driver = Driver.objects.get(id=id)

        if found_driver in drivers:

            title = f'Update Profile'

            if request.method == 'POST':

                # driver_form = NewDriver(request.POST)

                driver_profile_form = UpdateDriverProfile(
                    request.POST, instance=found_driver.driverprofile, files=request.FILES)

                if driver_profile_form.is_valid():

                    # driver_details = driver_form.save(commit=False)

                    driver_profile = driver_profile_form.save(commit=False)

                    driver_profile.driver = found_driver

                    driver_profile.profile_pic = driver_profile_form.cleaned_data['profile_pic']

                    driver_profile.car_image = driver_profile_form.cleaned_data['car_image']

                    driver_profile.save()

                    # driver_details.save()

                    return redirect(driver, found_driver.id)

                else:

                    messages.error(
                        request, ('Please correct the error below.'))

            else:

                # driver_form = NewDriver(instance=found_driver)

                driver_profile_form = UpdateDriverProfile(
                    instance=found_driver.driverprofile)

                return render(request, 'driver/update-profile.html', {"title": title, "driver": found_driver, "driver_profile_form": driver_profile_form})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        return redirect(new_driver)
        # raise Http404()


def driver_profile(request, passenger_id, driver_profile_id):
    '''
    View function to display list of driver profiles
    '''
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=passenger_id)

        if passenger in passengers:

            driver_profile = DriverProfile.objects.get(id=driver_profile_id)

            title = f'{driver_profile.driver.first_name} {driver_profile.driver.last_name}\'s Profile'

            reviews = DriverReview.get_driver_reviews(driver_profile_id)

            form = ReviewDriverForm()

            return render(request, "profile.html", {"title": title, "passenger": passenger, "driver_profile": driver_profile, "reviews": reviews, "form": form})

        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        return redirect(new_passenger)

        # raise Http404()


def review_driver(request, passenger_id, driver_profile_id):
    '''
    Function that saves a driver review without reloading the page
    '''
    passenger = Passenger.objects.get(id=passenger_id)

    driver_profile = DriverProfile.objects.get(id=driver_profile_id)

    review_content = request.POST.get('review_content')

    new_driver_review = DriverReview(
        passenger=passenger, driver_profile=driver_profile, review_content=review_content)

    new_driver_review.save()

    data = {'success': 'Your review has successfully been saved'}

    return JsonResponse(data)


def passenger_profile(request, driver_id, passenger_profile_id):
    '''
    View function to display list of driver profiles
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=driver_id)

        if driver in drivers:

            passenger_profile = PassengerProfile.objects.get(
                id=passenger_profile_id)

            title = f'{passenger_profile.passenger.first_name} {passenger_profile.passenger.last_name}\'s Profile'

            reviews = PassengerReview.get_passenger_reviews(
                passenger_profile_id)

            form = ReviewPassengerForm()

            return render(request, "driver/passenger-profile.html", {"title": title, "driver": driver, "passenger_profile": passenger_profile, "reviews": reviews, "form": form})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        return redirect(new_driver)

        # raise Http404()


def new_journey(request, driver_profile_id):
    '''
    View function to display a form for creating a new travel plan 
    '''
    title = "New Journey"

    try:

        driver_profile = DriverProfile.objects.get(id=driver_profile_id)

        found_driver = driver_profile.driver

        drivers = Driver.objects.all()

        if found_driver in drivers:

            if request.method == 'POST':

                form = NewTravelPlan(request.POST)

                if form.is_valid:

                    new_travel_plan = form.save(commit=False)

                    new_travel_plan.driver_profile = driver_profile

                    new_travel_plan.save()

                    return redirect(current_journey, found_driver.id)

                else:

                    messages.error(
                        request, ('Please correct the error below.'))

            else:

                form = NewTravelPlan()

                return render(request, 'all-drivers/new-journey.html', {"title": title, "form": form, "driver": found_driver})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        return redirect(new_driver)

        # raise Http404()


def current_journey(request, driver_id):
    '''
    View function to display a driver's travel plans
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=driver_id)

        if driver in drivers:

            driver_profile = driver.driverprofile

            travel_plans = TravelPlan.objects.filter(
                driver_profile=driver_profile)

            title = f'{driver.first_name} {driver.last_name}\'s Journeys'

            return render(request, 'drivers/current_journey.html', {"title": title, "driver": driver, "travel_plans": travel_plans, "driver_profile": driver_profile})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        return redirect(new_driver)
