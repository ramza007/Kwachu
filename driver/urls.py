from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.driverhome,name = 'home'),
    url(r'^new/', views.new_driver, name="newdriver"),
    url(r'^login/', views.driver_login, name="driverlogin"),
]