"""
main routes
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^driver/', include('driver.urls')),
    # url(r'^passanger/', include('passanger.urls')),
]
