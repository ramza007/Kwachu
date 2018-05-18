from django.shortcuts import render
from .forms import NewDriver, DriverLogin

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
                    # print('Not equal')
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
