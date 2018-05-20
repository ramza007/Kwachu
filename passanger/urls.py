from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.passanger, name='passanger'),
    url(r'^login/', views.passenger_login, name="passengerlogin"),
    url(r'^new/', views.new_passenger, name="newpassenger"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
