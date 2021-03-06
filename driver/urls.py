from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.driverhome,name = 'home'),
    url(r'^new/', views.new_driver, name="newdriver"),
    url(r'^login/', views.driver_login, name="driverlogin"),
    url( r'^profile/(\d+)/(\d+)', views.driver_profile, name="driverProfile"),
    url( r'^update/profile/(\d+)', views.update_driver_profile, name="updateDriverProfile"),
    url( r'^ajax/review-driver/profile/driver/(\d+)/(\d+)', views.review_driver, name="reviewDriver"),
    url( r'^profile/passenger/(\d+)/(\d+)', views.passenger_profile, name="passengerProfile"),
    url(r'^new/journey/(\d+)', views.new_journey, name="newJourney"),
    url(r'^journeys/(\d+)', views.current_journey, name="currentJourney"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
