from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.driverhome,name = 'home'),
    url(r'^new/', views.new_driver, name="newdriver"),
    url(r'^login/', views.driver_login, name="driverlogin"),
    url( r'^profile/driver/(\d+)/(\d+)', views.driver_profile, name="driverProfile"),
    # url( r'^update/passenger/profile/(\d+)', views.update_passenger_profile, name="updatePassengerProfile"),
]