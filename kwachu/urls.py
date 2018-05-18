"""
main routes
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^driver/', include('driver.urls')),
    url(r'^passanger/', include('passanger.urls')),
]
