from django.conf.urls import url
from . import views

urlpatterns=[
    url('^driver',views.driverhome,name = 'home'),
    url( r'^new/driver/', views.new_driver, name="newdriver"),
]