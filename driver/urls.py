from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.driverhome,name = 'home'),
    url(r'^new/driver/', views.new_driver, name="newdriver"),
    url(r'^login/driver/', views.driver_login, name="driverlogin"),
]